import pytest
from app import app 

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    print(response.data)  # Print the actual response for debugging
    assert b"Hello, DevOps Internship Task 2!" in response.data
