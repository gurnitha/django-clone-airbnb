# apps/rooms/admin.py

# Django modules
from django.contrib import admin

# Django locals
from apps.rooms import models

# Register your models here.
@admin.register(models.RoomType)

class ItemAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    pass