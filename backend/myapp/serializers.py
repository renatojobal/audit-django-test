from . import models
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
        

class RoleSerializer(ModelSerializer):
    class Meta:
        model = models.Role
        fields = '__all__'


class CitySerializer(ModelSerializer):
    class Meta:
        model = models.City
        fields = '__all__'
