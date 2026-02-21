from pydantic import BaseModel


class DietInput(BaseModel):
    Age: int
    Gender: str
    Height_cm: float
    Weight_kg: float
    BMI: float
    Chronic_Disease: str
    Blood_Pressure_Systolic: float
    Blood_Pressure_Diastolic: float
    Cholesterol_Level: float
    Blood_Sugar_Level: float
    Genetic_Risk_Factor: str
    Allergies: str
    Daily_Steps: float
    Exercise_Frequency: float
    Sleep_Hours: float
    Alcohol_Consumption: str
    Smoking_Habit: str
    Dietary_Habits: str
    Caloric_Intake: float
    Protein_Intake: float
    Carbohydrate_Intake: float
    Fat_Intake: float
    Preferred_Cuisine: str
    Food_Aversions: str


class PredictionOutput(BaseModel):
    prediction: str
