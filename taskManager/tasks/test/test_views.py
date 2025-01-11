from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from ..models import Task, Group, Comment
from rest_framework.authtoken.models import Token
from django.urls import reverse
from datetime import date, timedelta

class TaskViewSetTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            due_date=date.today() + timedelta(days=1),
            priority='Medium',
            status='Pending',
            created_by=self.user
        )

    def test_get_tasks(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        url = reverse('task-list')
        data = {
            'title': 'New Task',
            'description': 'New Description',
            'due_date': (date.today() + timedelta(days=1)).isoformat(),
            'priority': 'High',
            'status': 'Pending'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)
        self.assertEqual(Task.objects.get(id=response.data['id']).title, 'New Task')
