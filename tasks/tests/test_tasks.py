from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse

class TaskTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="pass123")
        login = self.client.post(reverse('token_obtain_pair'), {"username": "testuser", "password": "pass123"})
        self.token = login.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_create_task(self):
        url = "/tasks/"
        data = {"title": "Test Task", "description": "Testing", "completed": False}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_get_tasks(self):
        response = self.client.get("/tasks/")
        self.assertEqual(response.status_code, 200)
