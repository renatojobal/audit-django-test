from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework_simplejwt import authentication
from rest_framework import permissions
from rest_framework.response import Response
from .models import User

class UserAPI(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.s
    """
    # authentication_classes = [authentication.JWTTokenUserAuthentication] Creo que no es neceserio implmenetar ya que está especificado en settings
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)


