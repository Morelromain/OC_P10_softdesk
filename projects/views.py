from django.contrib.auth.models import Group
from rest_framework import viewsets, mixins
from rest_framework import permissions
from projects.serializers import UserSerializer, GroupSerializer, ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer
from .models import Project, Contributor, User, Issue, Comment

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited. 
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProjectPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if obj.author_user_id == request.user:
            return True
        readonly = False
        contributors = Contributor.objects.filter(project_id=obj.id)
        for contributor in contributors:
            if request.user == contributor.user_id :
                readonly = request.method in permissions.SAFE_METHODS
        return readonly


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
    permission_classes = [permissions.IsAuthenticated]

class IssuePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            id_p = view.kwargs.get("project_pk")
            try:
                contrib = Contributor.objects.get(user_id=request.user, project_id=id_p)
            except:
                return False
            if contrib.permission in ["Al", "Rd"]:
                return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            id_p = view.kwargs.get("project_pk")
            try:
                contrib = Contributor.objects.get(user_id=request.user, project_id=id_p)
            except:
                return False
            if contrib.permission == "Al":
                return True
            elif contrib.permission == "Rd":
                return request.method in permissions.SAFE_METHODS

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
    permission_classes = [permissions.IsAuthenticated]