"""Model loading and inference logic."""

import joblib
from .config import MODEL_PATH


def load_model():
    return joblib.load(MODEL_PATH)


model = load_model()
