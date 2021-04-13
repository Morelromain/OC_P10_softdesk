from rest_framework import permissions

from .models import Project, Contributor, User, Issue, Comment


class ProjectPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if obj.author_user_id == request.user:
            return True
        readonly = False
        contributors = Contributor.objects.filter(project_id=obj.id)
        for contributor in contributors:
            if request.user == contributor.user_id :
                readonly = request.method in permissions.SAFE_METHODS
        return readonly


class ContributorPermission(permissions.BasePermission):

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
                if request.user == obj.user_id:
                    return True
                else:
                    return request.method in permissions.SAFE_METHODS


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
                if request.user == obj.author_user_id:
                    return True
                else:
                    return request.method in permissions.SAFE_METHODS


class CommentPermission(permissions.BasePermission):

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
                if request.user == obj.author_user_id:
                    return True
                else:
                    return request.method in permissions.SAFE_METHODS