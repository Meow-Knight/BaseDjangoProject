from django.core.validators import MaxValueValidator, MinValueValidator

from api_account.models import Account
from api_base.models import TimeStampedModel
from django.db import models


class Lecture(TimeStampedModel):
    name = models.CharField(max_length=50)
    age = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    degree_grade = models.FloatField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="lectures")
