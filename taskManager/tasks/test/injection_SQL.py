from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class SQLInjectionTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_sql_injection_protection(self):
        response = self.client.get('/api/tasks/?search=1 OR 1=1')
        self.assertNotIn('all tasks', response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
