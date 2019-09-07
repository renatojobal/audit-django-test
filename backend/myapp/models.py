from django.db import models
from django.contrib.auth.models import AbstractUser


# La documemntación de los atributos se encuentra en el diagrama de entidades

# Inheriting from AbstractUser
class User(AbstractUser):
    """

    Attributes:

    idUser
    username provided by Django
    password provided by Django
    first_name provided by Django
    last_name provided by Django
    email provided by Django
    gender
    birthday
    points
    """
    # * PK
    idUser = models.AutoField(primary_key=True) 

    # * Atributos relacionales

    # * Otros atributos
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, default='U', blank=True)
    points = models.IntegerField(blank=True, null=True)


class City(models.User):
    """
    """
    # * PK
    idCity = models.AutoField(primary_key=True)

    # * Atributos relacionales

    # * Otros atributos
    name = models.CharField(max_length=100)


class TouristPoint(models.Model):
    """
    
    """
    # * PK
    idTouristPoint = models.AutoField(primary_key=True)

    # * Atributos relacionales

    # * Otros atributos
    name = models.CharField(max_length=100)
    latituded = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)


class Route(models.Model):
    """
    
    """
    # * PK
    idRoute = models.AutoFieldd(primary_key=True)

    # * Atributos relacionales

    # * Otros atributos
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)


class Restaurant(models.Model):
    """
    
    """
    # * PK
    idRestaurant = models.AutoField(primary_key=True)
    
    # * Atributos relacionales

    # * Otros atributos
    name = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)


class Prize(models.Model):
    """
    
    """
    # * PK
    idPrize = models.AutoField(primary_key=True)

    # * Atributos relacionales

    # * Otros atributos
    description = models.Tex


class UserRole(models.Model):
    """

    """

    # * PK
    idUserRole = models.AutoField(primary_key=True)
    
    # * Atributos relacionales

    # * Otros atributos
    state = models.BooleanField(default=True)



class Role(models.Model):
    """
    
    """

    # * PK
    idRole = models.AutoField(primary_key=True)
    
    # * Atributos relacionales

    # * Otros atributos
    name = models.CharField(max_length=100)
