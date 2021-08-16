from main import app
from tests import client


def test_prediction_diabetes_model():
    data = "0.07786339"
    response = client.post(f"/diabetes/test?data_diabetes={data}")
    res = response.json()
    assert "result" in res

    pred_val = res["result"]["prediction"]

    assert pred_val == 225.9732423295347
