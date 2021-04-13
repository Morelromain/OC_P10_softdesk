from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import Project, Contributor, Issue, Comment


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author_user_id']

class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['id','user_id', 'project_id', 'permission', 'role']

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id','title', 'desc', 'tag', 'priority', 'status', 'created_time', 'project_id', 'author_user_id', 'assignee_user_id']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'description', 'created_time', 'author_user_id', 'issue_id']