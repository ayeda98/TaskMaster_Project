from rest_framework import serializers
from .models import Task, Group, GroupMembership, Comment
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date

class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    assigned_to = serializers.StringRelatedField(read_only=True)
    progress = serializers.IntegerField(min_value=0, max_value=100)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority', 'status', 'created_by', 'assigned_to', 'progress', 'updated_at']

    def validate_due_date(self, value):
        if value < date.today():
            raise ValidationError("La date d'échéance ne peut pas être dans le passé.")
        return value

class GroupSerializer(serializers.ModelSerializer):
    leader = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'leader']

class GroupMembershipSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    group = GroupSerializer()

    class Meta:
        model = GroupMembership
        fields = ['id', 'user', 'group']

class CommentSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    task = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'task', 'content', 'created_at', 'created_by']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
