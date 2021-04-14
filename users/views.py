from rest_framework import viewsets
from rest_framework import permissions

from .serializers import UserSerializer
from .models import User

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser] 
    """permission_classes = [permissions.IsAuthenticated]"""

