# Django
from api.models import Profile

# Rest_framework
from rest_framework import viewsets

from api.serializers import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all().order_by('-date_joined')
    serializer_class = ProfileSerializer

