"""FastAPI main application file."""

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from .schemas import DietInput, PredictionOutput
from .utils import make_prediction


app = FastAPI()

# Prometheus instrumentation
Instrumentator().instrument(app).expose(app)


@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionOutput)
def predict(data: DietInput):
    """Prediction endpoint."""
    prediction = make_prediction(data.model_dump())
    return {"prediction": prediction}
