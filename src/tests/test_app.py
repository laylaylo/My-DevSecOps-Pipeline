import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"hostname" in response.data  # Check if hostname is in the response
    assert b"ip" in response.data  # Check if IP is in the response
