"""
Test App class to test app related functionalities
"""


class TestApp:
    """
    TestApp class
    """

    def test_app_homepage(self, client):
        """
        Test homepage is working
        """
        response = client.get("/")
        assert response.status_code == 302
