from django.db import models

from api_account.models import Lecture
from api_base.models import TimeStampedModel


class Course(TimeStampedModel):
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name="courses")
