from django.contrib.auth.models import Group
from rest_framework import viewsets, mixins
from rest_framework import permissions
from projects.serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer

from .models import Project, Contributor, Issue, Comment
from .perm import ProjectPermission, ContributorPermission, IssuePermission, CommentPermission

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# queryset à enlever quand def get_queryset?




class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [ProjectPermission]


class ContributorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [ContributorPermission]

    def get_queryset(self, *args, **kwargs):
        project = self.kwargs.get("project_pk")
        return Contributor.objects.filter(project_id=project)


class IssueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IssuePermission]

    def get_queryset(self, *args, **kwargs):
        project = self.kwargs.get("project_pk")
        return Issue.objects.filter(project_id=project)


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CommentPermission]

    def get_queryset(self, *args, **kwargs):
        issue = self.kwargs.get("issue_pk")
        return Comment.objects.filter(issue_id=issue)