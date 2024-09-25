import pytest
from src.counter import app
from src import status

@pytest.fixture()
def client():
    return app.test_client()

@pytest.mark.usefixtures("client")
class TestCounterEndPoints:

    def test_create_a_counter(self, client):
        """should create counter"""
        result = client.post('/counters/goo_create')
        assert result.status_code == status.HTTP_201_CREATED

    def test_duplicate_a_counter(self, client):
        """should return an error for duplicates"""
        result = client.post('/counters/goo_duplicate')
        assert result.status_code == status.HTTP_201_CREATED
        result = client.post('/counters/goo_duplicate')
        assert result.status_code == status.HTTP_409_CONFLICT

    def test_update_a_counter(self, client):
        """should update the counter"""
        result = client.post('/counters/goo_update')
        assert result.status_code == status.HTTP_201_CREATED
        
        result = client.put('/counters/goo_update')
        assert result.status_code == status.HTTP_200_OK
        assert result.json['goo_update'] == 1

    def test_read_a_counter(self, client):
        """should return the counter value"""
        result = client.post('/counters/goo_read')
        assert result.status_code == status.HTTP_201_CREATED
        
        result = client.get('/counters/goo_read')
        assert result.status_code == status.HTTP_200_OK
        assert result.json['goo_read'] == 0

    def test_read_non_existent_counter(self, client):
        """should return 404 for the non-existent counter"""
        result = client.get('/counters/does_not_exist')
        assert result.status_code == status.HTTP_404_NOT_FOUND

    def test_update_non_existent_counter(self, client):
        """should return 404 for updating a non-existent counter"""
        result = client.put('/counters/does_not_exist')
        assert result.status_code == status.HTTP_404_NOT_FOUND

    def test_delete_counter(self, client):
        """It should delete a counter"""
        # Create a counter first
        result = client.post('/counters/goo_delete')
        assert result.status_code == status.HTTP_201_CREATED
        # Delete the counter
        response = client.delete('/counters/goo_delete')
        assert response.status_code == status.HTTP_204_NO_CONTENT
        # Verify the counter is deleted
        result = client.get('/counters/goo_delete')
        assert result.status_code == status.HTTP_404_NOT_FOUND
