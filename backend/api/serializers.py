
# DJango utilities
from api.models import Profile

# Rest_framework utilitites
from rest_framework import serializers


# Utilidades de django
from django.contrib.auth.models import User


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('id')

    id = serializers.ReadOnlyField()
    phone_number = serializers.CharField()
    gender = serializers.CharField()
    birthday = serializers.DateField()
    picture = serializers.ImageField()

    created = serializers.DateField()
    modified = serializers.DateField()

    def create(self, validate_data):
        instance = Profile()
        # ! FIXME
        # instance.user = UserAPI()
        instance.phone_number = validate_data.get('phone_number')
        instance.gender = validate_data.get('gender')
        instance.birthday = validate_data.get('birthday')
        instance.save()

        return instance





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

    def validate_username(self, data):
        users = User.objects.filter(username=data)
        if len(users) !=0 :
            raise serializers.ValidationError("Este nombre de usuario ya existe. Ingrese uno nuevo")
        else:
            return data