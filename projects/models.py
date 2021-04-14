from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return 'Project: ' + self.title

class Contributor(models.Model):
    ALL = 'Al'
    READ = 'Rd'
    PERMISSION_CHOICES = [(ALL, 'All'), (READ, 'Read')]
    permission = models.CharField(max_length=2, choices=PERMISSION_CHOICES, default=ALL)
    role = models.CharField(max_length=128)

    user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return 'Contributor: ' + (self.user_id.username) + self.project_id.title

class Issue(models.Model):
    title = models.CharField(max_length=128)
    desc = models.CharField(max_length=128)
    tag = models.CharField(max_length=128)
    priority = models.CharField(max_length=128)
    status = models.CharField(max_length=128)
    created_time = models.DateTimeField(auto_now_add=True)

    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE, blank=True, null=True)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_id_author', blank=True, null=True)
    assignee_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_id_assignee', blank=True, null=True)

    def __str__(self):
        return 'Issue: ' + self.title

class Comment(models.Model):
    description = models.CharField(max_length=128)
    created_time = models.DateTimeField(auto_now_add=True)

    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    issue_id = models.ForeignKey(to=Issue, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return 'Comment: ' + self.description
