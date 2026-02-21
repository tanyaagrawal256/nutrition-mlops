import pandas as pd
from .model import model


def make_prediction(input_data: dict):
    """Make prediction using trained model."""
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)
    return prediction[0]
