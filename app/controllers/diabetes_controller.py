from app.services.diabetes_service import DiabetesService


class DiabetesController:
    def __init__(self) -> None:
        self.__diabetes_info_service = DiabetesService()

    def train(self):
        self.__diabetes_info_service.train_model()

    def test_model(self, data: float):
        return self.__diabetes_info_service.predict(data)
