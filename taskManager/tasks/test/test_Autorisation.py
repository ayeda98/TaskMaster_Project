from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class AuthenticationTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_access_without_authentication(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_access_with_authentication(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
