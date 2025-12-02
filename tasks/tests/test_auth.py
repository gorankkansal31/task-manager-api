from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthTests(APITestCase):

    def test_user_registration(self):
        url = reverse('register')
        data = {"username": "testuser", "password": "testpass123"}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_user_login(self):
        User.objects.create_user(username="testuser", password="testpass123")

        url = reverse('token_obtain_pair')
        data = {"username": "testuser", "password": "testpass123"}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
