from .models import User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        

class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'



