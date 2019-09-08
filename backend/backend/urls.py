from django.urls import include, path
from rest_framework import routers
from django.contrib import admin

from .router import router
urlpatterns = [

    # URLs de django apps
    path('admin/', admin.site.urls),

    # URLs de login_app
    path('', include(('login_app.urls'))),

    # URLs de myapp
    path('', include(router.urls)),
]
