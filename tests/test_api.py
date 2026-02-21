from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200


def test_predict_success():
    payload = {
       "Age": 30,
        "Gender": "Male",
        "Height_cm": 170,
        "Weight_kg": 70,
        "BMI": 24,
        "Chronic_Disease": "None",
        "Blood_Pressure_Systolic": 120,
        "Blood_Pressure_Diastolic": 80,
        "Cholesterol_Level": 180,
        "Blood_Sugar_Level": 90,
        "Genetic_Risk_Factor": "No",
        "Allergies": "None",
        "Daily_Steps": 8000,
        "Exercise_Frequency": 3,
        "Sleep_Hours": 7,
        "Alcohol_Consumption": "No",
        "Smoking_Habit": "No",
        "Dietary_Habits": "Vegetarian",
        "Caloric_Intake": 2000,
        "Protein_Intake": 80,
        "Carbohydrate_Intake": 250,
        "Fat_Intake": 70,
        "Preferred_Cuisine": "Indian",
        "Food_Aversions": "None"
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    assert "prediction" in response.json()


def test_predict_invalid_data():
    payload = {
        "Gender": "Male"
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 422


def test_metrics_endpoint():
    response = client.get("/metrics")
    assert response.status_code == 200


def test_docs_endpoint():
    response = client.get("/docs")
    assert response.status_code == 200