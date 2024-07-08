"""
Integration tests focus on testing the interaction between multiple components of the system. 
it aims to verify that the integrated parts of the application work together correctly.
"""

from fastapi.testclient import TestClient
from model_deployment.main import app

client = TestClient(app)


def test_prediction():
    url = "/predict"
    payload = {"Temperature": 25.0, "Oxygen": 21.0, "Humidity": 60.0}
    headers = {"Content-Type": "application/json"}

    response = client.post(url, json=payload, headers=headers)
    assert response.status_code == 200, "Response status code should be 200"
    result = response.json()
    assert "prediction" in result, "Response should contain 'prediction'"
    assert isinstance(
        result["prediction"], int
    ), "'prediction' should be an integer"
