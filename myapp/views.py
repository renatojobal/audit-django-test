from rest_framework.views import APIView
from rest_framework import viewsets
from .models import User, Role, City, UserRole, Restaurant, Prize, TouristPoint, Route, TouristPointRoute
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
    """
    Acepta los metodos: [POST, GET]

    Si el metodo es POST:
        Devuelve un json con la informacion del usuario y status = 201
    
    Si el metodo es GET:
        Devuelve un json con la informacion de tosos los usuarios y status = 200
    """
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

# ToDo: Crear vista que devuelva los puntos de un usuario en específico

# ToDo: Crear una vista que devuelva todas las rutas de un usuario en particular



@api_view(['GET', 'PUT', 'DELETE'])
def users_id(request, pk):
    """
    Acepta los metodos: [GET, PUT, DELETE]

    Si el metodo es GET:
        Devuelve un json con la informacion del usuario y status=200

    Si el metodo es PUT:
        Perminte modificar datos del usuario, devuelve un json con la info del usuario ya con las modificaciones y status=202

    Si el metodo es DELETE:
        Borra el usuario con el id dado en la url, devuelve un json con meta data y status = 202

    """
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
    """
    Acepta los metodos: [PUT]

    Si el metodo es PUT:
        Recibe en parametros: {"idUser", "points"}, y agrega los puntos al usuario con el id especificado. Status = 202
    """
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
    """
    Acepta los metodos: [POST]

    Si el metodos es POST:
        Crea un usuario con el rol turista y puntos = 0, status = 201
    """
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
    """
    Proporciona un CRUD general para el modelo de 'Role'
    """
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.AllowAny]

    queryset = Role.objects.all()
    serializer_class = serializers.RoleSerializer


class CityViewset(viewsets.ModelViewSet):
    """
    Proporciona un CRUD general para el modelo de 'City'
    """
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.AllowAny]

    queryset = City.objects.all()
    serializer_class = serializers.CitySerializer


class UserRoleViewset(viewsets.ModelViewSet):
    """
    Proporciona un CRUD general para el modelo de 'UserRole'
    """
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.AllowAny]

    queryset = UserRole.objects.all()
    serializer_class = serializers.UserRoleSerializer


class TouristPointRouteViewset(viewsets.ModelViewSet):
    """
    Proporciona un CRUD general para el modelo de 'UserRole'
    """
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.AllowAny]

    queryset = TouristPointRoute.objects.all()
    serializer_class = serializers.TouristPointRouteSerializer


class TouristPointViewset(viewsets.ModelViewSet):
    """
    Proporciona un CRUD general para el modelo de 'TouristPoint'
    """
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.AllowAny]

    queryset = TouristPoint.objects.all()
    serializer_class = serializers.TouristPointSerializer



class RouteViewset(viewsets.ModelViewSet):
    """
    Proporciona un CRUD general para el modelo de 'Route'
    """
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.AllowAny]

    queryset = Route.objects.all()
    serializer_class = serializers.RouteSerializer


class RestaurantViewset(viewsets.ModelViewSet):
    """
    Proporciona un CRUD general para el modelo de 'Restaurant'
    """
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.AllowAny]

    queryset = Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer


class PrizeViewset(viewsets.ModelViewSet):
    """
    Proporciona un CRUD general para el modelo de 'Prize'
    """
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.AllowAny]

    queryset = Prize.objects.all()
    serializer_class = serializers.PrizeSerializer
