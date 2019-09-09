from django.contrib import admin
from .models import User, Role

@admin.register(User)
class User(admin.ModelAdmin):

    list_display = ('username', 'first_name', 'last_name', 'email', 'gender', 'birthday', 'points', 'is_staff',)
    list_display_links = ('username', 'email',)
    list_editable = ('last_name', 'gender',)

    search_fields = ('username',)

    list_filter = ('points', 'is_staff', 'is_active',)

@admin.register(Role)
class User(admin.ModelAdmin):

    list_display =  ('name',)
    list_display_links = ('name',)

    search_fields = ('name',)


