import pytest
from src.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"hostname" in response.data
    assert b"<b>" in response.data and b"</b>" in response.data  # Check for the structure
