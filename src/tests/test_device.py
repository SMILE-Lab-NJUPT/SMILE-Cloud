import pytest 
from src.app import create_app 
from src.config.development import DevelopmentConfig

@pytest.fixture 
def client(): 
    app = create_app(DevelopmentConfig) 
    app.config['TESTING'] = True 
    with app.test_client() as client: 
        yield client

def test_send_command(client): 
    response = client.post('/api/devices/1/command', json={"action": "turn_on", "params": {"mode": "cooling", "temperature": 25}}) 
    assert response.status_code == 200 
    data = response.get_json() 
    assert data.get("new_state") == "on" 
