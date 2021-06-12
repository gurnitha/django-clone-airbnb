# apps/users/admin.py

# Django modules
from django.contrib import admin

# Import from local apps
from apps.users.models import User  # <-- it can be like this: from apps.users import Model

# Register your models here.

@admin.register(User) # <-- it equal to '@admin.register(models.User)'


class CustomUserAdmin(admin.ModelAdmin):
	pass 
