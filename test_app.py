import pytest
from app import app 

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    print(response.data)  
    assert b"Hello, DevOps Internship Task" in response.data
