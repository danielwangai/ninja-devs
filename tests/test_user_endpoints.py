import json

from tests import BaseTestCase


class TestUserEndpointsTestCase(BaseTestCase):
    def test_create_user(self):
        """
        Test that create user operation works
        """
        new_user = dict(username="dan", password="password")
        response = self.client.post(
            '/api/v1/auth/register',
            data=json.dumps(new_user)
        )
        self.assertEqual(response.status_code, 201)

    def test_create_user_rejects_duplicate_username(self):
        new_user = dict(username="dan", password="password")
        response = self.client.post(
            '/api/v1/auth/register',
            data=json.dumps(new_user)
        )
        self.assertEqual(response.status_code, 201)
        # create user with duplicated username
        new_user = dict(username="dan", password="password")
        response1 = self.client.post(
            '/api/v1/auth/register',
            data=json.dumps(new_user),
        )
        self.assertEqual(response.status_code, 409)
