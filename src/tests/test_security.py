import pytest 
from src.app import create_app 
from src.config.development import DevelopmentConfig

@pytest.fixture 
def client(): 
    app = create_app(DevelopmentConfig) 
    app.config['TESTING'] = True 
    with app.test_client() as client: 
        yield client

def test_get_face_logs(client): 
    response = client.get('/api/security/face_logs') 
    assert response.status_code == 200 
    data = response.get_json() 
    assert isinstance(data, list) 
