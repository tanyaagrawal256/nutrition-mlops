import streamlit as st
import requests

st.title("🥗 Nutrition Recommendation System")

st.header("Enter Your Details")

age = st.number_input("Age", min_value=1, max_value=100, value=30)
gender = st.selectbox("Gender", ["Male", "Female"])
height_cm = st.number_input("Height (cm)", value=170)
weight_kg = st.number_input("Weight (kg)", value=70)
bmi = st.number_input("BMI", value=24.0)

chronic_disease = st.selectbox("Chronic Disease", ["None", "Diabetes", "Hypertension"])

blood_pressure_systolic = st.number_input("Blood Pressure Systolic", value=120)
blood_pressure_diastolic = st.number_input("Blood Pressure Diastolic", value=80)

cholesterol_level = st.number_input("Cholesterol Level", value=180)
blood_sugar_level = st.number_input("Blood Sugar Level", value=90)

genetic_risk_factor = st.selectbox("Genetic Risk Factor", ["No", "Yes"])
allergies = st.selectbox("Allergies", ["None", "Peanuts", "Gluten"])

daily_steps = st.number_input("Daily Steps", value=8000)
exercise_frequency = st.number_input("Exercise Frequency (per week)", value=3)
sleep_hours = st.number_input("Sleep Hours", value=7)

alcohol_consumption = st.selectbox("Alcohol Consumption", ["No", "Yes"])
smoking_habit = st.selectbox("Smoking Habit", ["No", "Yes"])

dietary_habits = st.selectbox("Dietary Habits", ["Vegetarian", "Non-Vegetarian"])

caloric_intake = st.number_input("Caloric Intake", value=2000)
protein_intake = st.number_input("Protein Intake", value=80)
carbohydrate_intake = st.number_input("Carbohydrate Intake", value=250)
fat_intake = st.number_input("Fat Intake", value=70)

preferred_cuisine = st.selectbox("Preferred Cuisine", ["Indian", "Continental", "Asian"])
food_aversions = st.selectbox("Food Aversions", ["None", "Spicy", "Dairy"])

if st.button("Get Recommendation"):

    payload = {
        "Age": age,
        "Gender": gender,
        "Height_cm": height_cm,
        "Weight_kg": weight_kg,
        "BMI": bmi,
        "Chronic_Disease": chronic_disease,
        "Blood_Pressure_Systolic": blood_pressure_systolic,
        "Blood_Pressure_Diastolic": blood_pressure_diastolic,
        "Cholesterol_Level": cholesterol_level,
        "Blood_Sugar_Level": blood_sugar_level,
        "Genetic_Risk_Factor": genetic_risk_factor,
        "Allergies": allergies,
        "Daily_Steps": daily_steps,
        "Exercise_Frequency": exercise_frequency,
        "Sleep_Hours": sleep_hours,
        "Alcohol_Consumption": alcohol_consumption,
        "Smoking_Habit": smoking_habit,
        "Dietary_Habits": dietary_habits,
        "Caloric_Intake": caloric_intake,
        "Protein_Intake": protein_intake,
        "Carbohydrate_Intake": carbohydrate_intake,
        "Fat_Intake": fat_intake,
        "Preferred_Cuisine": preferred_cuisine,
        "Food_Aversions": food_aversions
    }

    response = requests.post("https://nutrition-mlops.onrender.com/predict", json=payload)

    if response.status_code == 200:
        prediction = response.json()["prediction"]
        st.success(f"Recommended Diet: {prediction}")
    else:
        st.error("Error connecting to API")