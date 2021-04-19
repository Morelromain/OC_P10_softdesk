from rest_framework import serializers
from .models import Project, Contributor, Issue, Comment


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author_user_id']
        read_only_fields = ['author_user_id']

    def create(self, validated_data):
        """Add author contributor automatically when create."""
        info_p = Project.objects.create(**validated_data)
        info_p.author_user_id = self.context["request"].user
        info_p.save()
        Contributor.objects.create(
            user_id=self.context["request"].user,
            project_id=info_p,
            permission="Al",
            role="Author"
            )
        return info_p


class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = ['id', 'title', 'desc', 'tag', 'priority',
                  'status', 'created_time', 'project_id',
                  'author_user_id', 'assignee_user_id']
        read_only_fields = ['author_user_id', 'project_id']

    def create(self, validated_data):
        info_i = Issue.objects.create(**validated_data)
        info_i.author_user_id = self.context["request"].user
        if info_i.assignee_user_id is None:
            info_i.assignee_user_id = info_i.author_user_id
        info_i.save()
        return info_i


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'description', 'created_time',
                  'author_user_id', 'issue_id']
        read_only_fields = ['author_user_id', 'issue_id']

    def create(self, validated_data):
        info_i = Comment.objects.create(**validated_data)
        info_i.author_user_id = self.context["request"].user
        info_i.save()
        return info_i


class ContributorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['id', 'user_id', 'project_id', 'permission', 'role']
        read_only_fields = ['project_id']
