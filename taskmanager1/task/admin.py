from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active')
    ordering = ('email',)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Task)
admin.site.register(Category)
