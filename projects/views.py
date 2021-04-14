from rest_framework import viewsets

from .serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer
from .models import Project, Contributor, Issue, Comment
from .perm import ProjectPermission, ContributorPermission, IssuePermission, CommentPermission


class ProjectViewSet(viewsets.ModelViewSet):
    """API endpoint that allows Project to be viewed or edited."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [ProjectPermission]

    """def create(self, request):
        request.data.update({"author_user_id": request.user.id})
        print(super().create(request))
        return super().create(request)"""

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

    def perform_create(self, serializer, *args, **kwargs):
        project_pk = self.kwargs['project_pk']
        project = Project.objects.get(pk= project_pk)
        serializer.save(project_id=project)

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
