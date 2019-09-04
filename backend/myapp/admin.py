from django.contrib import admin
from .models import User

@admin.register(User)
class User(admin.ModelAdmin):

    list_display = ('username', 'first_name', 'last_name', 'email', 'gender', 'birthday', 'points',)
    list_display_links = ('username', 'email',)
    list_editable = ('last_name', 'gender',)

    search_fields = ('username',)

    list_filter = ('points', 'is_staff', 'is_active',)