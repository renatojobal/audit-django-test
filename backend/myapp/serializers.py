from . import models
from rest_framework import serializers 


class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()
    is_staff = serializers.BooleanField()
    is_superuser = serializers.BooleanField()
    date_joined = serializers.ReadOnlyField()
    birthday = serializers.DateField()
    gender = serializers.CharField()
    points = serializers.IntegerField()
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
    class Meta:
        model = models.Role
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = '__all__'

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserRole
        fields = '__all__'