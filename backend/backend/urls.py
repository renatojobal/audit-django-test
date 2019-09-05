from django.urls import include, path
from rest_framework import routers
from django.contrib import admin


urlpatterns = [

    # URLs de django apps
    path('admin/', admin.site.urls),

    # URLs de login_app
    path('login_app/', include(('login_app.urls'))),

    # URLs de myapp
    path('myapp/', include(('myapp.urls'))),
]
