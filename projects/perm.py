from rest_framework import permissions

from .models import Contributor


class ProjectPermission(permissions.BasePermission):
    """
    Permission for all to view his project or create a new one.
    Permission for author to modificate/delete project.
    """

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        try:
            info_c = Contributor.objects.get(
                user_id=request.user, project_id=obj
                )
        except Contributor.DoesNotExist:
            return False

        if info_c.permission == "Al":
            return True
        elif info_c.permission == "Rd":
            return request.method in permissions.SAFE_METHODS


class ContributorPermission(permissions.BasePermission):
    """
    Permission for all to view his project's contributors.
    Permission for project's author to modificate/delete contributors
    to his projects or create a new one.
    """

    def has_permission(self, request, view):
        id_p = view.kwargs.get("project_pk")
        try:
            info_c = Contributor.objects.get(
                user_id=request.user, project_id=id_p
                )
        except Contributor.DoesNotExist:
            return False
        if info_c.permission in ["Al", "Rd"]:
            return True

    def has_object_permission(self, request, view, obj):
        id_p = view.kwargs.get("project_pk")
        try:
            info_c = Contributor.objects.get(
                user_id=request.user, project_id=id_p
                )
        except Contributor.DoesNotExist:
            return False
        if info_c.permission == "Al":
            return request.method in ["DELETE"]
        elif info_c.permission == "Rd":
            if request.user == obj.user_id:
                return True
            else:
                return request.method in permissions.SAFE_METHODS


class IssueandComPermission(permissions.BasePermission):
    """
    Permission for all to view his project's issues or create a new one.
    Permission for issue's author to modificate/delete his issue.
    """

    def has_permission(self, request, view):
        id_p = view.kwargs.get("project_pk")
        try:
            info_c = Contributor.objects.get(
                user_id=request.user, project_id=id_p
                )
        except Contributor.DoesNotExist:
            return False
        if info_c.permission in ["Al", "Rd"]:
            return True

    def has_object_permission(self, request, view, obj):
        id_p = view.kwargs.get("project_pk")
        try:
            info_c = Contributor.objects.get(
                user_id=request.user, project_id=id_p
                )
        except Contributor.DoesNotExist:
            return False
        if info_c.permission == "Al":
            return True
        elif info_c.permission == "Rd":
            if request.user == obj.author_user_id:
                return True
            else:
                return request.method in permissions.SAFE_METHODS
