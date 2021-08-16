from main import app
from tests import client


def test_app_info():
    response = client.get("/")
    res = response.json()

    assert response.status_code == 200
    assert "app_name" in res
    assert res["version"] == "0.0.1"
    assert "models" in res
