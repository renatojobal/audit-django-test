from . import models
from rest_framework import serializers 


class UserSerializer(serializers.Serializer):
    """
    Serializador customizado para el modelo 'User'
    Aqui se escribe por defecto los puntos en 0, asi se especifique otro valor, este no sera tomado en cuenta.
    ESto con la finalidad de que todos los usuarios se inicialicen en 0 y no exista incongruencias.
    """
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()
    is_staff = serializers.BooleanField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    date_joined = serializers.ReadOnlyField()
    birthday = serializers.DateField()
    gender = serializers.CharField()
    points = serializers.IntegerField(read_only=True)
    #groups = serializers.ReadOnlyField()
    #user_permissions = serializers.ReadOnlyField()
    password = serializers.CharField()

    def create(self, validate_data):
        instance = models.User()
        instance.first_name = validate_data.get('first_name')
        instance.last_name = validate_data.get('last_name')
        instance.username = validate_data.get('username')
        instance.email = validate_data.get('email')
        instance.is_staff = False
        instance.is_superuser = False
        instance.birthday = validate_data.get('birthday')
        instance.gender = validate_data.get('gender')
        instance.points = 0
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance

    def add_points(self, user, points):
        instance = user
        instance.points += int(points)
        return instance
    
    def validate_username(self, data):
        users = models.User.objects.filter(username = data)
        if len(users) != 0:
            raise serializers.ValidationError("ESte nombre de usuario ya existe. Ingrese uno nuevo")
        else:
            return data
        

class UserModelSerializer(serializers.ModelSerializer):
    """
    Actualmente esta despreciado este serializador, deberias usar UserSerializer
    """
    class Meta:
        model = models.User
        fields = '__all__'



class RoleSerializer(serializers.ModelSerializer):
    """
    Serializazdor que hereda de serializers.ModelSerializer
    en metadatos se le especifica el modelo de 'Role'
    """
    class Meta:
        model = models.Role
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    """
    Serializazdor que hereda de serializers.ModelSerializer
    en metadatos se le especifica el modelo de 'City'
    """
    class Meta:
        model = models.City
        fields = '__all__'

class UserRoleSerializer(serializers.ModelSerializer):
    """
    Serializazdor que hereda de serializers.ModelSerializer
    en metadatos se le especifica el modelo de 'UserRole'
    """
    class Meta:
        model = models.UserRole
        fields = '__all__'

class TouristPointRouteSerializer(serializers.ModelSerializer):
    """
    Serializazdor que hereda de serializers.ModelSerializer
    en metadatos se le especifica el modelo de 'TouristPointRoute'
    """
    class Meta:
        model = models.TouristPointRoute
        fields = '__all__'

class TouristPointSerializer(serializers.ModelSerializer):
    """
    Serializazdor que hereda de serializers.ModelSerializer
    en metadatos se le especifica el modelo de 'TouristPoint'
    """
    class Meta:
        model = models.TouristPoint
        fields = '__all__'

class RouteSerializer(serializers.ModelSerializer):
    """
    Serializazdor que hereda de serializers.ModelSerializer
    en metadatos se le especifica el modelo de 'Route'
    """
    class Meta:
        model = models.Route
        fields = '__all__'

class RestaurantSerializer(serializers.ModelSerializer):
    """
    Serializazdor que hereda de serializers.ModelSerializer
    en metadatos se le especifica el modelo de 'Restaurant'
    """
    class Meta:
        model = models.Restaurant
        fields = '__all__'

class PrizeSerializer(serializers.ModelSerializer):
    """
    Serializazdor que hereda de serializers.ModelSerializer
    en metadatos se le especifica el modelo de 'Prize'
    """
    class Meta:
        model = models.Prize
        fields = '__all__'
