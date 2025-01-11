from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class XSSTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_xss_protection(self):
        response = self.client.post('/api/comments/', {
            'task': 1,
            'content': '<script>alert("XSS Attack")</script>',
            'created_by': self.user.id
        }, format='json')
        self.assertNotIn('<script>', response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
