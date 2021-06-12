# # apps/users/admin.py

# # Django modules
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

# # Import from local apps
# from apps.users.models import User  # <-- it can be like this: from apps.users import Model

# # Register your models here.

# @admin.register(User) # <-- it equal to '@admin.register(models.User)'


# class CustomUserAdmin(admin.ModelAdmin):

#     """ Custom User Admin """

#     list_display = ("username", "email", "gender", "language", "currency", "superhost")
#     list_filter = ("language", "currency", "superhost")

# ----new---

# apps/users/admin.py

# Django modules
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Import from local apps
from apps.users.models import User  # <-- it can be like this: from apps.users import Model

# Register your models here.

@admin.register(User) # <-- it equal to '@admin.register(models.User)'

class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
