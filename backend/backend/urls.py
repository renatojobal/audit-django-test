from django.urls import include, path
from rest_framework import routers
from api.api import ProfileAPI, UserAPI
from django.contrib import admin



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/1.0/create_profile', ProfileAPI.as_view(), name = "api_create_profile"),
    path('api/1.0/create_user/', UserAPI.as_view(), name = 'api_create_user'),
]
