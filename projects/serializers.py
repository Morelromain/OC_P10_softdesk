from rest_framework import serializers
from .models import Project, Contributor, Issue, Comment


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author_user_id']
        read_only_fields = ['author_user_id']

    def create(self, validated_data):
        print(validated_data)
        info_p = Project.objects.create(**validated_data)
        info_p.author_user_id = self.context["request"].user
        info_p.save()
        return info_p

    '''def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)'''

class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['id','user_id', 'project_id', 'permission', 'role']

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id','title', 'desc', 'tag', 'priority', 
                  'status', 'created_time', 'project_id', 
                  'author_user_id', 'assignee_user_id']
        read_only_fields = ['author_user_id', 'project_id']

    def create(self, validated_data):
        info_i = Issue.objects.create(**validated_data)
        info_i.author_user_id = self.context["request"].user
        info_i.save()
        return info_i




class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'description', 'created_time', 
                  'author_user_id', 'issue_id']