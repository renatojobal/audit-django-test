from django.db import models
from django.contrib.auth.models import AbstractUser


# La documemntación de los atributos se encuentra en el diagrama de entidades





class City(models.Model):
    """
    """
    # * PK
    # idCity = models.AutoField(primary_key=True)

    # * Atributos relacionales

    # * Otros atributos
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)


    def __unicode__(self):
	    return self.name

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()


class TouristPoint(models.Model):
    """
    
    """
    # * PK
    # idTouristPoint = models.AutoField(primary_key=True)

    # * Atributos relacionales
    city = models.ForeignKey(to=City, on_delete=models.CASCADE)

    # * Otros atributos
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    latituded = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)

    def __unicode__(self):
	    return self.name

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()



# Inheriting from AbstractUser
class User(AbstractUser):
    """

    Attributes:

    # idUser
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
    # idUser = models.AutoField(primary_key=True) 

    # * Atributos relacionales


    # * Otros atributos
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, default='U', blank=True)
    points = models.IntegerField(blank=True, null=True, default=0)


    def __unicode__(self):
	    return self.username

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()

class Role(models.Model):
    """
    
    """

    # * PK
    # idRole = models.AutoField(primary_key=True) # ! Using the default
    
    # * Atributos relacionales
    users = models.ManyToManyField(User, through='UserRole')

    # * Otros atributos
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)

    def __unicode__(self):
	    return self.name

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()


class Route(models.Model):
    """
    
    """
    # * PK
    # idRoute = models.AutoField(primary_key=True)

    # * Atributos relacionales
    touristPoints = models.ManyToManyField(to=TouristPoint, through='TouristPointRoute')
    users = models.ManyToManyField(to=User)

    # * Otros atributos
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    score = models.IntegerField(default=0)


    def __unicode__(self):
	    return self.name

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()

class TouristPointRoute(models.Model):
    """
    Tabla customizada de la relazion muchos a muchos entre Rout y TouristPoint
    """
    # * PK
    # Por defecto

    # * Atributos relacionales
    touristPoint = models.ForeignKey(to=TouristPoint, on_delete=models.CASCADE)
    route = models.ForeignKey(to=Route, on_delete=models.PROTECT)

    # * Otros atributos


    def __unicode__(self):
        string = "%s pertenece a %s" % (self.touristPoint, self.route)
        return string

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()


class UserRole(models.Model):
    """
    Tabla customizada de la relacion muchos a muchos entre User y Role
    """

    # * PK
    # idUserRole = models.AutoField(primary_key=True)
    
    # * Atributos relacionales
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    role = models.ForeignKey(to=Role, on_delete=models.PROTECT)

    # * Otros atributos
    state = models.BooleanField(default=True)

    def __unicode__(self):
        string = "%s pertenence al rol %s" % (self.user, self.role)
        return string

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()

class Restaurant(models.Model):
    """
    
    """
    # * PK
    # idRestaurant = models.AutoField(primary_key=True)
    
    # * Atributos relacionales
    user = models.ForeignKey(to=User, on_delete=models.PROTECT)
    city = models.ForeignKey(to=City, on_delete=models.DO_NOTHING)
    

    # * Otros atributos
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    radio = models.IntegerField(default=100, blank=False, null=False)

    def __unicode__(self):
	    return self.name

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()


class Prize(models.Model):
    """
    
    """
    # * PK
    # idPrize = models.AutoField(primary_key=True)

    # * Atributos relacionales
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)
    users = models.ManyToManyField(to=User) 

    # * Otros atributos
    description = models.CharField(max_length=300, blank=False, null=False, unique=True)
    pointsRequired = models.IntegerField(default=0)

    def __unicode__(self):
        string = self.description
        cutted_string = string[0:20]
        new_string = "%s..." % (cutted_string)
        return new_string

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()



