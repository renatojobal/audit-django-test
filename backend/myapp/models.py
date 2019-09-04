from django.db import models
from django.contrib.auth.models import AbstractUser

# Inheriting from AbstractUser
class User(AbstractUser):
    """

    Attributes:

    idUser equal to id from Django
    username provided by Django
    password provided by Django
    first_name provided by Django
    last_name provided by Django
    email provided by Django
    gender
    birthday
    points
    """
    
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, default='U', blank=True)
    points = models.IntegerField(blank=True, null=True)
