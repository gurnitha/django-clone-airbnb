# apps/users/models.py

# Django modules
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    bio = models.TextField(default="")