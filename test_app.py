import pytest
from app import app, dias_vividos


def test_dias_vividos():
    assert dias_vividos(10) == 3650


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Calcula los d\xc3\xadas vividos' in response.data


def test_index_post_valid(client):
    response = client.post('/', data={'nombre': 'Guillermo', 'edad': '25'})
    assert response.status_code == 200
    assert b'Guillermo, has vivido aproximadamente' in response.data


def test_index_post_invalid(client):
    response = client.post('/', data={'nombre': 'Guillermo', 'edad': 'abc'})
    assert response.status_code == 200
    assert b'Error: La edad debe ser un n\xc3\xbamero entero.' in response.data
