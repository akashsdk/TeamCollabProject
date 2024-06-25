from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='teamcollab_user_set',  # Changed related name to avoid conflicts
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='teamcollab_user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='teamcollab_user_set',  # Changed related name to avoid conflicts
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='teamcollab_user'
    )

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_projects')
    created_at = models.DateTimeField(auto_now_add=True)

class ProjectMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=[('Admin', 'Admin'), ('Member', 'Member')])

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[('To Do', 'To Do'), ('In Progress', 'In Progress'), ('Done', 'Done')])
    priority = models.CharField(max_length=10, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='tasks')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
