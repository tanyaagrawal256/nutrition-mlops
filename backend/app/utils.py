"""Utility functions for prediction."""

import pandas as pd
from .model import model


def make_prediction(data: dict):
    """Make prediction using trained model."""
    if model is None:
        return "Model not available"

    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return prediction[0]
