from django.contrib import admin
from .models import City, TouristPoint, User, Role, Route, UserRole, Restaurant, Prize

# @admin.register(User)
# class User(admin.ModelAdmin):
#     """
#     Customizando la informacion que se vera en el admin site de django
#     """
#     list_display = ('username', 'first_name', 'last_name', 'email', 'gender', 'birthday', 'points', 'is_staff',)
#     list_display_links = ('username', 'email',)
#     list_editable = ('last_name', 'gender',)

#     search_fields = ('username',)

#     list_filter = ('points', 'is_staff', 'is_active',)




# * Registro de modelos con las funciones por defecto
admin.site.register(City)
admin.site.register(TouristPoint)
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Route)
admin.site.register(UserRole)
admin.site.register(Restaurant)
admin.site.register(Prize)