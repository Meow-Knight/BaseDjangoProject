from django.db import models

from api_account.models.Role import Role
from api_base.models import TimeStampedModel


class Account(TimeStampedModel):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    avatar = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="accounts")
