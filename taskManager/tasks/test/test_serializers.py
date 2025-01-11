from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Task, Group, Comment
from ..serializers import TaskSerializer, GroupSerializer, CommentSerializer

class TaskSerializerTest(TestCase):

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

    def test_task_serializer(self):
        serializer = TaskSerializer(instance=self.task)
        data = serializer.data
        self.assertEqual(data['title'], 'Test Task')
        self.assertEqual(data['status'], 'Pending')

class GroupSerializerTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='group_leader', password='testpass')
        self.group = Group.objects.create(name='Test Group', leader=self.user)

    def test_group_serializer(self):
        serializer = GroupSerializer(instance=self.group)
        data = serializer.data
        self.assertEqual(data['name'], 'Test Group')
        self.assertEqual(data['leader'], 'group_leader')

class CommentSerializerTest(TestCase):

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

    def test_comment_serializer(self):
        serializer = CommentSerializer(instance=self.comment)
        data = serializer.data
        self.assertEqual(data['content'], 'Test Comment')
        self.assertEqual(data['created_by'], 'commenter')
