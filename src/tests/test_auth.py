import pytest 
from src.app import create_app 
from src.config.development import DevelopmentConfig

@pytest.fixture 
def client(): 
    app = create_app(DevelopmentConfig) 
    app.config['TESTING'] = True 
    with app.test_client() as client: 
        yield client

def test_login(client): 
    response = client.post('/api/auth/login', json={"username": "alice", "password": "123456"}) 
    assert response.status_code == 200 
    data = response.get_json() 
    assert "token" in data 
