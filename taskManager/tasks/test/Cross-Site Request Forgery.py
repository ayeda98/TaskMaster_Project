from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class CSRFAttackTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_csrf_protection(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post('/api/tasks/', {
            'title': 'Test Task',
            'description': 'Description',
            'due_date': '2023-12-31',
            'priority': 'High',
            'status': 'Pending'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
