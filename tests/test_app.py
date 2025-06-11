import io
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_index_page(client):
    rv = client.get('/')
    assert b'Detec' in rv.data

def test_upload_endpoint_missing_files(client):
    rv = client.post('/upload', data={}, content_type='multipart/form-data')
    assert rv.status_code == 400

def test_upload_endpoint(client):
    data = {
        'video': (io.BytesIO(b'data'), 'test.mp4'),
        'template': (io.BytesIO(b'data'), 'test.jpg'),
        'threshold': '0.5'
    }
    rv = client.post('/upload', data=data, content_type='multipart/form-data')
    assert rv.data.decode() == 'Processando...'
