from rest_framework.views import APIView
from rest_framework import viewsets
from .models import User, Role, City, UserRole
from . import serializers
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import json

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


@api_view(['GET'])
def users_id(request, pk):
    if request.method == 'GET':
        """
        Devolver el usuario con el id seleccionado
        """

        queryset = User.objects.filter(id=pk)

        serializer = serializers.UserModelSerializer(queryset.get())

        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        """
        Actualizar el usuario
        """
        queryset = User.objects.filter(id=pk)
        serializer = serializers.UserModelSerializer(queryset.get())
        if serializer.is_valid():
            user = serializer.update()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        """
        Borrar el usuario con el id dado
        """
        queryset = User.objects.filter(id=pk)
        serializer = serializers.UserModelSerializer(queryset.get())
        if serializer.is_valid():
            result = queryset.delete()
            return Response(result, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def add_points(request):
    if request.method == 'PUT':
        """
        Sumar los puntos enviados
        """

        body = request.data
        user_id = int(body['idUser'])
        points_to_add = int(body['points'])

        queryset = User.objects.filter(id=user_id)

        # ? Agregamos los puntos directamente sin usar points
        
        user = queryset.get()
        user.points += points_to_add
        user.save()
        serializer = serializers.UserModelSerializer(user)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def tourist_user(request):
    if request.method == 'POST':

        """
        Agregamos un usuario como un nuevo turista
        """

        # Obtenemos el rol que corresponda con turista
        querysetRoles = Role.objects.filter(name='tourist')
        
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            


class RoleViewset(viewsets.ModelViewSet):

    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.AllowAny]

    queryset = Role.objects.all()
    serializer_class = serializers.RoleSerializer


class CityViewset(viewsets.ModelViewSet):

    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.AllowAny]

    queryset = City.objects.all()
    serializer_class = serializers.CitySerializer


class UserRoleViewset(viewsets.ModelViewSet):

    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.AllowAny]

    queryset = UserRole.objects.all()
    serializer_class = serializers.UserRoleSerializer
