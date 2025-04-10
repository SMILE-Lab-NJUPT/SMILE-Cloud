import pytest 
from src.app import create_app 
from src.config.development import DevelopmentConfig

@pytest.fixture 
def client(): 
    app = create_app(DevelopmentConfig) 
    app.config['TESTING'] = True 
    with app.test_client() as client: 
        yield client

def test_get_latest_sensor(client): 
    response = client.get('/api/sensors/1/latest') 
    assert response.status_code == 200 
    data = response.get_json() 
    assert data.get("device_id") == 1

def test_get_sensor_history(client):
    response = client.get('/api/sensors/1/history?start=2025-03-30T00:00:00Z&end=2025-03-31T00:00:00Z') 
    assert response.status_code == 200 
    data = response.get_json() 
    assert isinstance(data, list)
