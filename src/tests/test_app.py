import pytest
from src.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"hostname" in response.data  # Check if hostname is in the response
    assert b"<b>10.1.0.62</b>" in response.data  # Adjusted to match the HTML structure
