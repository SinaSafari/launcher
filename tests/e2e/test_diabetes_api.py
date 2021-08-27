import os
from main import app
from tests import client


def test_prediction_diabetes_model():
    data = "0.07786339"
    response = client.post(f"/api/v1/diabetes/test?data_diabetes={data}")
    res = response.json()
    assert "result" in res

    pred_val = res["result"]["prediction"]

    assert pred_val == 225.9732423295347


def test_model_file_exists():
    model_file_path = f"{os.getcwd()}/storage/diabetes.model"
    assert os.path.isfile(model_file_path)
