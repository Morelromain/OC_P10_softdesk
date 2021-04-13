from django.contrib.auth.models import Group
from rest_framework import viewsets, mixins
from rest_framework import permissions
from users.serializers import UserSerializer

from .models import User

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
    permission_classes = [permissions.IsAdminUser]
    """permission_classes = [permissions.IsAuthenticated]"""
