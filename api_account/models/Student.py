from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from api_account.models import Account
from api_base.models import TimeStampedModel


class Student(TimeStampedModel):
    name = models.CharField(max_length=50)
    age = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    address = models.CharField(max_length=250)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="students")

