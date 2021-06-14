import pytest
from fastapi.testclient import TestClient


from app import app


def test_homepage():
    with TestClient(app) as client:
        response = client.get('/')
        assert response.status_code == 200
        assert "Hello" in response.json()


def test_predict(dataset_example):
    with TestClient(app) as client:
        response = client.get('/predict', json=dataset_example)
    assert response.status_code == 200

    result = [data["target"] for data in response.json()]
    assert any([0 in result, 1 in result])
    assert len(set(result)) < 3

