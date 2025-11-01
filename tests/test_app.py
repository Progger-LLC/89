import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    """Test the index page loads successfully."""
    response = client.get('/')
    assert response.status_code == 200

def test_execute_code(client):
    """Test the code execution endpoint."""
    response = client.post('/execute', json={"code": "print('Hello, World!')"})
    data = response.get_json()
    assert response.status_code == 200
    assert data['output'] == "Hello, World!"

def test_syntax_error(client):
    """Test the execution of invalid code."""
    response = client.post('/execute', json={"code": "print('Hello, World!'"})
    data = response.get_json()
    assert response.status_code == 200
    assert "SyntaxError" in data['error_message']