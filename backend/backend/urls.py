from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
from myapp import views

from .router import router
urlpatterns = [

    # URLs de django apps
    path('admin/', admin.site.urls),

    # URLs de login_app
    path('', include(('login_app.urls'))),

    # URLs de myapp
    path('', include(router.urls)),
    path('users/', views.users),
    path('users/<int:pk>/', views.users_id),
    path("addPoints/", views.add_points),
]
