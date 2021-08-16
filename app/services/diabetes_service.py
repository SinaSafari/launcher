import os
from typing import Dict
import joblib
import numpy as np
from joblib import load
from lib.diabetes_model import train_diabetes_model


class DiabetesService:
    def __init__(self) -> None:
        self.model_path = f"{os.getcwd()}/storage/diabetes.model"

    def train_model(self) -> None:
        train_diabetes_model()

    def predict(self, data_diabetes: float) -> Dict[str, float]:
        model = joblib.load(self.model_path)
        data = np.array([[data_diabetes]])
        prediction = model.predict(data)
        return {"prediction": prediction[0]}
