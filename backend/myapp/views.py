from rest_framework.views import APIView
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

class UserViewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class RoleViewset(viewsets.ModelViewSet):
    queryset = models.Role.objects.all()
    serializer_class = serializers.RoleSerializer

