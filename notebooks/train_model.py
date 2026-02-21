import wandb
import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

# 🔴 Paste your Neon connection string here
connection_string = "postgresql://neondb_owner:npg_u9o0mjYZrKGL@ep-super-term-a1vhyv6l.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

engine = create_engine(connection_string)

# Load from Neon
df = pd.read_sql("SELECT * FROM nutrition_data", engine)

print("Data loaded from Neon:", df.shape)

# 🔹 Drop data leakage columns
df = df.drop(columns=[
    "Patient_ID",
    "Recommended_Calories",
    "Recommended_Protein",
    "Recommended_Carbs",
    "Recommended_Fats"
])

# 🔹 Define target
y = df["Recommended_Meal_Plan"]
X = df.drop(columns=["Recommended_Meal_Plan"])

print(X.columns.tolist())

print("Class Distribution:")
print(df["Recommended_Meal_Plan"].value_counts())

# 🔹 Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 🔹 Separate numeric & categorical
num_cols = X.select_dtypes(include=["int64", "float64"]).columns
cat_cols = X.select_dtypes(include=["object"]).columns

# 🔹 Preprocessing
preprocessor = ColumnTransformer([
    ("num", StandardScaler(), num_cols),
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
])

# 🔹 Create pipeline
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestClassifier())
])

print("Pipeline created successfully!")


from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import accuracy_score, f1_score

wandb.init(
    project="nutrition-mlops",
    config={
        "model": "RandomForest",
        "n_iter": 4,
        "cv": 3
    }
)

# 🔹 Hyperparameters
params = {
    "model__n_estimators": [100, 200],
    "model__max_depth": [None, 10, 20]
}

# 🔹 Randomized Search
search = RandomizedSearchCV(
    pipeline,
    params,
    cv=3,
    n_iter=4,
    scoring="f1_weighted",
    n_jobs=-1
)

print("Training model...")

search.fit(X_train, y_train)

print("Training completed!")

# 🔹 Predictions
y_pred = search.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average="weighted")

wandb.log({
    "accuracy": accuracy,
    "f1_score": f1,
    "best_n_estimators": search.best_params_["model__n_estimators"],
    "best_max_depth": search.best_params_["model__max_depth"]
})

print("Accuracy:", accuracy)
print("F1 Score:", f1)
print("Best Parameters:", search.best_params_)

import joblib

joblib.dump(search.best_estimator_, "../backend/best_model.joblib")

print("Best model saved to backend folder.")


artifact = wandb.Artifact("diet-model", type="model")
artifact.add_file("../backend/best_model.joblib")
wandb.log_artifact(artifact)

wandb.finish()