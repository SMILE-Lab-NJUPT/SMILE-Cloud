import pytest 
from src.app import create_app 
from src.config.development import DevelopmentConfig

@pytest.fixture 
def client(): 
    app = create_app(DevelopmentConfig) 
    app.config['TESTING'] = True 
    with app.test_client() as client: 
        yield client

def test_change_system_mode(client): 
    response = client.post('/api/system/mode', json={"mode": "night", "enable": True}) 
    assert response.status_code == 200 
    data = response.get_json() 
    assert data.get("active") == True
