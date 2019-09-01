# DJango utilities
from api.models import Profile

# Rest_framework utilitites
from rest_framework import serializers


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('id')

    def create(self, validated_data):
        instance = Profile(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.save()
        return instance

