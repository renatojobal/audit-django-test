# Django
from django.urls import include, path
from rest_framework import routers
from .views import Logout
from rest_framework.authtoken import views # Utilizo el login propio de rest_framework


urlpatterns = [
    path('login/', views.obtain_auth_token, name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]


