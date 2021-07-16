from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
from myapp import views

from .router import router
urlpatterns = [

    # URLs de django apps
    path('8wd4ds5ad4w8d4644qd8s/', admin.site.urls),

    # URLs de login_app
    path('', include(('login_app.urls'))),

    # URLs de myapp
    path('', include(router.urls)),
    path('users/', views.users),
    path('users/<int:pk>/', views.users_id),
    path("addPoints/", views.add_points),
    path("touristUser/", views.tourist_user),
]
