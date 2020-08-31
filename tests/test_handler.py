import pytest
from api.main import app
from fastapi.testclient import TestClient


@pytest.fixture()
def test_client():
    return TestClient(app)


def test_simple(test_client):
    response = test_client.get("/simple")
    assert response.status_code == 200
    assert response.json() == {'Hello': 'World'}


def test_stats(test_client):
    response = test_client.get("/stats/?numbers=5&numbers=6")
    expected = {'nobs': 2, 'mean': 5.5, 'minmax': [5, 6], 'skewness': 0.0, 'variance': 0.5, 'kurtosis': -2.0}
    assert expected == response.json()
