"""Model loading logic."""

import os
import joblib

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "../best_model.joblib"
)


def load_model():
    """Load trained model if available."""
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return None


model = load_model()
