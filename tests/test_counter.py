import pytest
from src.counter import app  # Import the app (Flask or similar framework) that manages the counter functionality
from src import status  # Import status codes (HTTP responses)

# Fixture to initialize a test client for the Flask app
# This client simulates requests to the application without starting an actual web server
@pytest.fixture()
def client():
    return app.test_client()

# Class that contains all test cases related to counter endpoints
# Using 'client' fixture for all tests in the class
@pytest.mark.usefixtures("client")
class TestCounterEndPoints:

    def test_create_a_counter(self, client):
        """
        Test case for creating a new counter.
        This test sends a POST request to create a new counter 
        and verifies that the server responds with a 201 Created status.
        """
        result = client.post('/counters/goo_create')
        assert result.status_code == status.HTTP_201_CREATED

    def test_duplicate_a_counter(self, client):
        """
        Test case for handling duplicate counters.
        First, a counter is created, which should return 201 Created.
        A second attempt to create the same counter should return 409 Conflict,
        indicating a duplicate.
        """
        result = client.post('/counters/goo_duplicate')
        assert result.status_code == status.HTTP_201_CREATED
        result = client.post('/counters/goo_duplicate')
        assert result.status_code == status.HTTP_409_CONFLICT

    def test_update_a_counter(self, client):
        """
        Test case for updating an existing counter.
        First, a counter is created with a POST request (201 Created).
        Then, the counter value is updated using a PUT request (200 OK).
        Verifies that the counter's new value is as expected.
        """
        result = client.post('/counters/goo_update')
        assert result.status_code == status.HTTP_201_CREATED
        
        result = client.put('/counters/goo_update')  # Update the counter
        assert result.status_code == status.HTTP_200_OK
        assert result.json['goo_update'] == 1  # Check if the updated value is correct

    def test_read_a_counter(self, client):
        """
        Test case for reading the current value of a counter.
        First, a counter is created (201 Created), then the counter value is read (200 OK).
        Verifies that the initial value of the counter is correct.
        """
        result = client.post('/counters/goo_read')
        assert result.status_code == status.HTTP_201_CREATED
        
        result = client.get('/counters/goo_read')  # Get the counter value
        assert result.status_code == status.HTTP_200_OK
        assert result.json['goo_read'] == 0  # Verify the initial value of the counter

    def test_read_non_existent_counter(self, client):
        """
        Test case for trying to read a counter that does not exist.
        Sends a GET request for a non-existent counter, and expects a 404 Not Found status.
        """
        result = client.get('/counters/does_not_exist')
        assert result.status_code == status.HTTP_404_NOT_FOUND

    def test_update_non_existent_counter(self, client):
        """
        Test case for updating a non-existent counter.
        Sends a PUT request to update a counter that has not been created, expecting a 404 Not Found status.
        """
        result = client.put('/counters/does_not_exist')
        assert result.status_code == status.HTTP_404_NOT_FOUND

    def test_delete_counter(self, client):
        """
        Test case for deleting an existing counter.
        First, creates a new counter (201 Created), then deletes it (204 No Content).
        Finally, attempts to retrieve the deleted counter and verifies it is not found (404 Not Found).
        """
        # Create a counter first
        result = client.post('/counters/goo_delete')
        assert result.status_code == status.HTTP_201_CREATED
        # Delete the counter
        response = client.delete('/counters/goo_delete')
        assert response.status_code == status.HTTP_204_NO_CONTENT
        # Verify the counter is deleted
        result = client.get('/counters/goo_delete')
        assert result.status_code == status.HTTP_404_NOT_FOUND
    
    def test_delete_non_existent_counter(self, client):
        """
        Test case for deleting a counter that doesn't exist.
        Sends a DELETE request to a non-existent counter, expecting a 404 Not Found status.
        """
        result = client.delete('/counters/non_existent_counter')
        assert result.status_code == status.HTTP_404_NOT_FOUND
