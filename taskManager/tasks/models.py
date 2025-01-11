from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date

# Validation pour s'assurer que la date d'échéance n'est pas dans le passé
def validate_due_date(value):
    if value < date.today():
        raise ValidationError("La date d'échéance ne peut pas être dans le passé.")

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField(validators=[validate_due_date])
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='Pending')
    created_by = models.ForeignKey(User, related_name='created_tasks', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, related_name='assigned_tasks', on_delete=models.SET_NULL, null=True, blank=True)
    progress = models.IntegerField(default=0)

    # Ajouter un champ updated_at pour suivre les mises à jour
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.progress < 0 or self.progress > 100:
            raise ValidationError({'progress': "Le progrès doit être entre 0 et 100."})

    def __str__(self):
        return self.title

class Group(models.Model):
    name = models.CharField(max_length=100)
    leader = models.ForeignKey(User, related_name='led_groups', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class GroupMembership(models.Model):
    group = models.ForeignKey(Group, related_name='memberships', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='group_memberships', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.group.name}"

class Comment(models.Model):
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.created_by.username} on {self.task.title}"
