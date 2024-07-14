from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)  # second option
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'identifier']

# admin.site.register(CustomUser, UserAdmin)   # first option
