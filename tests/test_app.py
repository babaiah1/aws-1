import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_health(client):
    res = client.get('/health')
    assert res.status_code == 200
    assert res.get_json() == {'status': 'ok'}

def test_echo(client):
    res = client.post('/echo', json={'msg': 'hello'})
    assert res.status_code == 200
    assert res.get_json()['received']['msg'] == 'hello'
