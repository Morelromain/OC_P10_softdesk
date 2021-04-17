from rest_framework import viewsets
from rest_framework import permissions

from .serializers import UserSerializer
from .models import User


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in ('POST')


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows create user only."""
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [UserPermission]
