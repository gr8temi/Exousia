from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import register, Change_detail
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
	add_form = register
	form=Change_detail
	model=CustomUser

	list_display=['username', 'email', 'first_name', 'last_name']

admin.site.register(CustomUser,CustomUserAdmin)