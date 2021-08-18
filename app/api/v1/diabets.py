from fastapi import APIRouter
from app.controllers.diabetes_controller import DiabetesController

router = APIRouter(prefix="/diabetes")


@router.get("/train")
def train_model_api():
    controller = DiabetesController()
    controller.train()
    return {"message": "done"}


@router.post("/test")
def predict_model_api(data_diabetes: float):
    controller = DiabetesController()
    result = controller.test_model(data_diabetes)
    return {"result": result}
