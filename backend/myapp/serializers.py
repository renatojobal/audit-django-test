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



