from rest_framework import viewsets
from rest_framework import permissions

from .models import Project, Contributor, Issue, Comment
from .serializers import (
    ProjectSerializer, ContributorSerializer,
    IssueSerializer, CommentSerializer
)
from .perm import (
    ProjectPermission, ContributorPermission, IssueandComPermission
)


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Projects to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [ProjectPermission & permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        contributors = Contributor.objects.filter(user_id=self.request.user)
        info_p = [contributor.project_id.id for contributor in contributors]
        return Project.objects.filter(id__in=info_p)


class ContributorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Contributors to be viewed or edited.
    """
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [ContributorPermission & permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        project = self.kwargs.get("project_pk")
        return Contributor.objects.filter(project_id=project)

    def perform_create(self, serializer, *args, **kwargs):
        project_pk = self.kwargs['project_pk']
        project = Project.objects.get(pk=project_pk)
        serializer.save(project_id=project)


class IssueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Issues to be viewed or edited.
    """
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IssueandComPermission & permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        project = self.kwargs.get("project_pk")
        return Issue.objects.filter(project_id=project)

    def perform_create(self, serializer, *args, **kwargs):
        project_pk = self.kwargs['project_pk']
        project = Project.objects.get(pk=project_pk)
        serializer.save(project_id=project)


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Comments to be viewed or edited.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IssueandComPermission & permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        issue = self.kwargs.get("issue_pk")
        return Comment.objects.filter(issue_id=issue)

    def perform_create(self, serializer, *args, **kwargs):
        issue_pk = self.kwargs['issue_pk']
        issue = Issue.objects.get(pk=issue_pk)
        serializer.save(issue_id=issue)
