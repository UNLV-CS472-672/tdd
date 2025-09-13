"""
Test Cases for Counter Web Service

Create a service that can keep a track of multiple counters
- API must be RESTful - see the status.py file. Following these guidelines, you can make assumptions about
how to call the web service and assert what it should return.
- The endpoint should be called /counters
- When creating a counter, you must specify the name in the path.
- Duplicate names must return a conflict error code.
- The service must be able to update a counter by name.
- The service must be able to read the counter
Counter API Implementation
"""

import pytest
from src import app
from src import status

@pytest.fixture()
def client():
    """Fixture for Flask test client"""
    return app.test_client()

@pytest.mark.usefixtures("client")
class TestCounterEndpoints:
    """Test cases for Counter API"""
    def test_create_counter(self, client):
        """It should create a counter"""
        result = client.post('/counters/foo')
        assert result.status_code == status.HTTP_201_CREATED
        
        
    def test_get_nonexistent_counter_returns_404(self, client):
        """It should return 404 when getting a counter that does not exist"""
        result = client.get('/counters/doesnotexist')
        assert result.status_code == status.HTTP_404_NOT_FOUND

        
    # def test_counter_exists_helper(self):
    #     """It should return True if counter exists, False otherwise"""
    #     from src import COUNTERS, counter_exists

    #     # Make sure dict is clean
    #     COUNTERS.clear()

    #     assert counter_exists("foo") is False  # not created yet

    #     COUNTERS["foo"] = 0
    #     assert counter_exists("foo") is True   # now it exists

            
    # def nonexistent_counter_returns_404(self, client):
    #     # GET /counters/<name> should return 404 if counter does not exist
    #     response = client.get("/counters/doesnotexist")
    #     assert response.status_code == status.HTTP_404_NOT_FOUND
    #     assert response.json == {"error": "Counter doesnotexist not found"}

