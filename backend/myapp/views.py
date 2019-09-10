from rest_framework.views import APIView
from rest_framework import viewsets
from .models import User, Role, City, UserRole
from . import serializers
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# class UserViewset(viewsets.ModelViewSet):

#     authentication_classes = [JWTTokenUserAuthentication]
#     permission_classes = [permissions.AllowAny]l

#     queryset = User.objects.all()
#     serializer_class = serializers.UserSerializer



@api_view(['POST', 'GET'])
def users(request):
    if request.method == 'POST':
        """
        Crear el nuevo usuario con 0 puntos
        """
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        """
        Obtener una lista de todos los usasurios
        """
        queryset = User.objects.all()
        serializer = serializers.UserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



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