from rest_framework.views import APIView
from rest_framework import viewsets
from myapp.models import User, Role
from . import serializers
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

class UserViewset(viewsets.ModelViewSet):

    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.AllowAny]

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class RoleViewset(viewsets.ModelViewSet):

    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.AllowAny]

    queryset = Role.objects.all()
    serializer_class = serializers.RoleSerializer

