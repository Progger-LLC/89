import json
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_execute_code_valid(client):
    response = client.post('/execute', json={'code': 'print("Hello, World!")'})
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['output'] == "Hello, World!\n"

def test_execute_code_invalid(client):
    response = client.post('/execute', json={'code': 'print("Hello, World!'})
    data = json.loads(response.data)
    assert response.status_code == 500
    assert 'SyntaxError' in data['error_message']

def test_execute_code_no_input(client):
    response = client.post('/execute', json={})
    data = json.loads(response.data)
    assert response.status_code == 400
    assert data['error_message'] == "No code provided"