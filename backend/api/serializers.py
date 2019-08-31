
# Utilidades de rest_framework
from rest_framework import serializers

# Utilidades de django
from django.contrib.auth.models import User

# Claso para traducir el usuario
class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()


    def create(self, validate_data):
        instance = User()
        instance.first_name = validate_data.get('first_name')
        instance.last_name = validate_data.get('last_name')
        instance.username = validate_data.get('username')
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.save()

        return instance

    def validate_username(self, username):
        users = User.object.filter(username = username)
        if len(users) !=0 :
            raise serializers.ValidationError("Este nombre de usuario ya existe. Ingrese uno nuevo")
        else:
            return username