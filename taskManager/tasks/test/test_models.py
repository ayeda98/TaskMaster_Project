from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date, timedelta
from ..models import Task, Group, GroupMembership, Comment

class TaskModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            due_date=date.today() + timedelta(days=1),
            priority='Medium',
            status='Pending',
            created_by=self.user
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.status, 'Pending')
        self.assertEqual(self.task.created_by, self.user)

    def test_due_date_validation(self):
        past_date = date.today() - timedelta(days=1)
        with self.assertRaises(ValidationError):
            task = Task(
                title='Past Task',
                description='Description',
                due_date=past_date,
                priority='High',
                status='Pending',
                created_by=self.user
            )
            task.full_clean()

class GroupModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='group_leader', password='testpass')
        self.group = Group.objects.create(name='Test Group', leader=self.user)

    def test_group_creation(self):
        self.assertEqual(self.group.name, 'Test Group')
        self.assertEqual(self.group.leader, self.user)

class CommentModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='commenter', password='testpass')
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            due_date=date.today() + timedelta(days=1),
            priority='Medium',
            status='Pending',
            created_by=self.user
        )
        self.comment = Comment.objects.create(
            task=self.task,
            content='Test Comment',
            created_by=self.user
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.content, 'Test Comment')
        self.assertEqual(self.comment.created_by, self.user)
        self.assertEqual(self.comment.task, self.task)
