import json

from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from music.models import Songs
from django.contrib.auth.models import User

class BaseViewTest(APITestCase):
    client = APIClient()


    @staticmethod
    def create_song(title="", artist=""):
        if title != "" and artist != "":
            Songs.objects.create(title=title, artist=artist)

    def login_a_user(self, username="", password=""):
        url = reverse(
            "auth-login",
            kwargs={
                "version":"v1"
            }
        )
        return self.client.post(
            url,
            data=json.dumps({
                "username": username,
                "password": password
            }),
            content_type="application/json"
        )

    def setUp(self):
        # create a admin user
        self.user = User.objects.create_superuser(
            username="test_user",
            email="test@mail.com",
            password="testing",
            first_name="test",
            last_name="user",
        )
        self.create_song("like glue", "sean paul")
        self.create_song("simple song", "konshens")
        self.create_song("love is wicked", "brick and lace")
        self.create_song("jam rock", "damien marley")

class GetAllSongsTest(BaseViewTest):

    def test_get_all_songs(self):

        response= self.client.get(
            reverse("songs-all", kwargs={"version": "v1"})
        )


class AuthLoginUserTest(BaseViewTest):
    """
      Tests for the auth/login/ endpoint
    """
    def test_login_user_with_valid_credentials(self):
        #test login with valid credentials
        response = self.login_a_user('test_user', "testing")

        #assert token key exists
        self.assertIn("token", response.data)

        #assert status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.login_a_user("anonymous", "pass")
        # assert status code is 401 UNAUTHORIZED
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
