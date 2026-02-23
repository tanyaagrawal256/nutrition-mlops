🥗 Nutrition Recommendation System – MLOps Project  

🚀 Overview  

This project is an end-to-end MLOps pipeline for a Nutrition Recommendation System.  

The system:  
	•	Takes user health & lifestyle inputs  
	•	Uses a trained ML model  
	•	Deploys via FastAPI  
	•	Monitors with Prometheus & Grafana  
	•	Includes CI/CD with GitHub Actions  
	•	Deployed on Render (Backend + Frontend)  

This demonstrates a complete production-style ML lifecycle.  

⸻  

🧠 Problem Statement  

Design and deploy a machine learning system that:  
	•	Predicts personalized diet recommendations  
	•	Exposes API endpoints  
	•	Implements monitoring  
	•	Applies CI/CD  
	•	Deploys to cloud  

⸻  

🏗️ System Architecture  

```
User → Streamlit Frontend → FastAPI Backend → ML Model (.joblib)  
                               ↓  
                       Prometheus Metrics  
                               ↓  
                            Grafana
```  

📂 Project Structure  

```nutrition-mlops/  
│  
├── backend/  
│   ├── app/  
│   │   ├── main.py  
│   │   ├── model.py  
│   │   ├── schemas.py  
│   │   ├── utils.py  
│   │   └── config.py  
│   ├── best_model.joblib  
│   ├── requirements.txt  
│   └── Dockerfile  
│
├── frontend/  
│   ├── app.py  
│   └── requirements.txt  
│
├── tests/  
│   └── test_api.py  
│
├── .github/workflows/  
│   └── ci.yml  
│
├── docker-compose.yml  
├── prometheus.yml  
└── README.md
```

🤖 Machine Learning  
	•	Model: Scikit-learn classifier  
	•	Saved as: best_model.joblib  
	•	Input features:  
	•	Gender  
	•	BMI  
	•	Exercise frequency  
	•	Sleep hours  
	•	Lifestyle habits  
	•	Macronutrient intake  
	Output:  
	•	Recommended Diet Category  

⸻  

🌐 Backend – FastAPI  
	•	Framework: FastAPI  
	•	Endpoint: /predict  
	•	Auto docs: /docs  
	•	Instrumented with:  
	•	prometheus-fastapi-instrumentator
	•	Metrics exposed at:
	•	/metrics

Example API Request  

```
{  
  "Gender": "Male",  
  "Height_cm": 170,  
  "Weight_kg": 70,  
  "BMI": 24,  
  "Chronic_Disease": "None",  
  "Blood_Pressure_Systolic": 120,  
  "Blood_Pressure_Diastolic": 80,  
  "Blood_Sugar_Level": 90,  
  "Genetic_Risk_Factor": "No",  
  "Allergies": "None",  
  "Daily_Steps": 8000,  
  "Exercise_Frequency": 3,  
  "Sleep_Hours": 7,  
  "Alcohol_Consumption": "No",  
  "Smoking_Habit": "No",  
  "Dietary_Habits": "Vegetarian",  
  "Preferred_Cuisine": "Indian",  
  "Food_Aversions": "None"  
}
``` 

🖥️ Frontend – Streamlit  

Interactive UI that:  
	•	Accepts health & diet inputs  
	•	Calls FastAPI /predict  
	•	Displays recommendation  
	•	Handles backend wake-up (free tier cold start)  

⸻  

📊 Monitoring  

Prometheus  
	•	Scrapes /metrics  
	Tracks:  
	•	Total API requests  
	•	Request rate  
	•	Latency  
	•	5xx errors  

Grafana Dashboards  

Created dashboards:  
	1.	Total API Requests  
	2.	Requests per second  
	3.	Average API Latency  
	4.	5xx Error Rate  

⸻  

🧪 Testing  
	•	Framework: Pytest  
	•	5 unit tests implemented  
	•	Covers:  
	•	Health endpoint  
	•	Successful prediction  
	•	Validation errors  
	•	Schema correctness  
	•	API behavior  

⸻  

🧹 Code Quality  
	•	Flake8: All major lint issues resolved  
	•	Pylint Score: 8+/10  
	•	Modular structure maintained  

⸻  

🔁 CI/CD – GitHub Actions  

On every push to main:  
	1.	Install dependencies  
	2.	Run Flake8  
	3.	Run Pytest  
	4.	Ensure build stability  

Workflow file:  

```
.github/workflows/ci.yml
```

🐳 Dockerization  

Backend containerized using:  

```
python:3.10-slim
```    

Includes:  
	•	FastAPI  
	•	Uvicorn  
	•	ML dependencies  

Used for:  
	•	Local deployment  
	•	Prometheus monitoring  
	•	Production-style testing  

☁️ Deployment  

Backend (Render)  

Live URL:  

```
https://nutrition-mlops.onrender.com
```

Swagger:  

/docs  

Frontend (Render)  

Live URL:  

```
https://nutrition-mlops-frontend.onrender.com
``` 

🧩 Challenges Faced  
	•	Model file missing in production  
	•	Git ignore rules blocking .joblib  
	•	Free tier cold-start delays  
	•	CORS configuration  
	•	CI path issues  

All resolved successfully.  

⸻  

📈 Business Value  

This system demonstrates:  
	•	Deployable ML models  
	•	Scalable API architecture  
	•	Production monitoring  
	•	Automated testing & CI/CD  
	•	Cloud deployment readiness  

Suitable for:  
	•	Digital health startups  
	•	Nutrition tech platforms  
	•	Preventive healthcare analytics    

⸻  

👩‍💻 Author  

Tanya Agrawal  
PGDM – AI & Data Science in Healthcare  
IIHMR Bangalore  

