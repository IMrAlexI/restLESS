from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=12, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return '{}'.format(self.email)
