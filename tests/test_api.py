import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_run_code_success(client):
    response = client.post('/execute', json={"code": "print('Hello, World!')"})
    assert response.status_code == 200
    assert response.json['output'] == "Hello, World!"
    assert response.json['error_message'] is None

def test_run_code_syntax_error(client):
    response = client.post('/execute', json={"code": "print('Hello, World!'"})
    assert response.status_code == 400
    assert response.json['output'] == ""
    assert "SyntaxError" in response.json['error_message']

def test_run_code_invalid_json(client):
    response = client.post('/execute', data="invalid json")
    assert response.status_code == 400
    assert "No code provided" in response.json['error']['message']