from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    pass

class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return 'Project: ' + self.title

class Contributor(models.Model):
    AUTHOR = 'AU'
    RESPONSIBLE = 'RE'
    CREATOR = 'CR'
    PERMISSION_CHOICES = [
        (AUTHOR, 'Author'),
        (RESPONSIBLE, 'Responsible'),
        (CREATOR, 'Creator'),
    ]
    permission = models.CharField(
        max_length=2,
        choices=PERMISSION_CHOICES,
        default=AUTHOR,
    )
    role = models.CharField(max_length=128)

    user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE)

    def __str__(self):
        return 'Contributor: ' + self.user_id + self.project_id

class Issue(models.Model):
    title = models.CharField(max_length=128)
    desc = models.CharField(max_length=128)
    tag = models.CharField(max_length=128)
    priority = models.CharField(max_length=128)
    status = models.CharField(max_length=128)
    created_time = models.DateTimeField(auto_now_add=True)

    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_id_author')
    assignee_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_id_assignee')

    def __str__(self):
        return 'Issue: ' + self.title

class Comment(models.Model):
    description = models.CharField(max_length=128)
    created_time = models.DateTimeField(auto_now_add=True)

    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue_id = models.ForeignKey(to=Issue, on_delete=models.CASCADE)

    def __str__(self):
        return 'Comment: ' + self.comment_id
