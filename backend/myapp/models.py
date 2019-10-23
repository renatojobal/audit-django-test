from django.db import models
from django.contrib.auth.models import AbstractUser


# La documemntación de los atributos se encuentra en el diagrama de entidades

class City(models.Model):
    """
    Modelo de ciudad
    """
    # * PK
    # id = Generado automaticamente

    # * Atributos relacionales

    # * Otros atributos
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)


    def __unicode__(self):
	    return self.name

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = "ciudad"
        verbose_name_plural = "ciudades"

class TouristPoint(models.Model):
    """
    
    """
    # * PK
    # id = Generado por automaticamente

    # * Atributos relacionales
    city = models.ForeignKey(to=City, on_delete=models.CASCADE)

    # * Otros atributos
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    latituded = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    radio = models.IntegerField(blank=False, null=False, default=100)  # Radio en metros

    def __unicode__(self):
	    return self.name

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()
    
    class Meta:
        verbose_name = "punto turistico"
        verbose_name_plural = "puntos turisticos"



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
    # id = Generado automaticamente

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
    
    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"

class Role(models.Model):
    """
    
    """

    # * PK
    # id = Generado automaticamente
    
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
    
    class Meta:
        verbose_name = "rol"
        verbose_name_plural = "roles"


class Route(models.Model):
    """
    """
    # * PK
    # id = Generado automaticamente

    # * Atributos relacionales
    touristPoints = models.ManyToManyField(to=TouristPoint, through='TouristPointRoute')
    users = models.ManyToManyField(to=User, through='UserRoute')

    # * Otros atributos
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    score = models.IntegerField(default=0)


    def __unicode__(self):
	    return self.name

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()
    
    class Meta:
        verbose_name = "ruta"
        verbose_name_plural = "rutas"

class TouristPointRoute(models.Model):
    """
    Tabla customizada de la relazion muchos a muchos entre Rout y TouristPoint
    """
    # * PK
    # id = Generado automaticamente

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
    
    class Meta:
        verbose_name = "punto turistico y ruta"
        verbose_name_plural = "puntos turisticos y rutas"


class UserRole(models.Model):
    """
    Tabla customizada de la relacion muchos a muchos entre User y Role
    """

    # * PK
    # id = Generado automaticamente
    
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
    
    
    class Meta:
        verbose_name = "usuario y rol"
        verbose_name_plural = "usuarios y roles"


class UserRoute(models.Model):
    """
    Tabla customizada de la relacion muchos a muchos entre User y Route
    """

    # * PK
    # id = Generado automaticamente
    
    # * Atributos relacionales
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    route = models.ForeignKey(to=Route, on_delete=models.PROTECT)

    # * Otros atributos
    state = models.BooleanField(default=True)

    def __unicode__(self):
        string = "%s pertenence a la ruta %s" % (self.user, self.route)
        return string

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()
    
    
    class Meta:
        verbose_name = "usuario y ruta"
        verbose_name_plural = "usuarios y rutas"


class Restaurant(models.Model):
    """
    
    """
    # * PK
    # id = Generado automaticamente
    
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

    class Meta:
        verbose_name = "restaurante"
        verbose_name_plural = "restaurantes"

class Prize(models.Model):
    """
    
    """
    # * PK
    # id = Generado automaticamente
    
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

    class Meta:
        verbose_name = "premio"
        verbose_name_plural = "premios"
        


