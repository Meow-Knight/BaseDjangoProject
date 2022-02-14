from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='uploads/%Y/%m', null=True)

    USERNAME_FIELD = 'username'

    class Meta:
        db_table = 'account'
