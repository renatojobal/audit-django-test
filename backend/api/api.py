
from rest_framework.response import Response
from .serializers import ProfileSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework import status


class ProfileAPI(APIView):

    def post(self, request):
        serializer = ProfileSerializer( data = request.data )
        if serializer.is_valid():
            profile = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserAPI(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    

