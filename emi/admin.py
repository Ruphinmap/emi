from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from emi.models import CustomUser
from django.contrib import admin


class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser,UserModel)