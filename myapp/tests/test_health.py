def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Healthy'