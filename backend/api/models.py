
# Django
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    # Modelo proxy que extendera el modelo por defecto de usuario

    # Relacionamos el modelo con el proxy model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=20, default='Unknown')
    birthday = models.DateField()
    picture = models.ImageField(upload_to='users/picture', blank=True, null=True)

    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username