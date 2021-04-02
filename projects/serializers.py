from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import Project, Contributor, User, Issue, Comment


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'user_id', 'username', 'first_name', 'last_name', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['project_id', 'title', 'description', 'type']

class ContributorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contributor
        fields = ['user_id', 'project_id', 'permission', 'role']

class IssueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contributor
        fields = ['title', 'desc', 'tag', 'priority', 'status', 'created_time', 'project_id', 'author_user_id', 'assignee_user_id']

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contributor
        fields = ['comment_id', 'description', 'created_time', 'author_user_id', 'issue_id']