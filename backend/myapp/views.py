from rest_framework.views import APIView
from rest_framework import viewsets
from .models import User, Role, City, UserRole
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
    permission_classes = [permissions.IsAdminUser]

    queryset = Role.objects.all()
    serializer_class = serializers.RoleSerializer


class CityViewset(viewsets.ModelViewSet):

    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.IsAdminUser]

    queryset = City.objects.all()
    serializer_class = serializers.CitySerializer


class UserRoleViewset(viewsets.ModelViewSet):

    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.IsAdminUser]

    queryset = UserRole.objects.all()
    serializer_class = serializers.UserRoleSerializer
