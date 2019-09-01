# DJango utilities
from api.models import Profile

# Rest_framework utilitites
from rest_framework import serializers


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['url', 'username', 'email', 'groups']

