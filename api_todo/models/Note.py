from django.db import models

from api_base.models import TimeStampedModel
from api_todo.models import User


class Note(TimeStampedModel):
    class Meta:
        db_table = 'note'

    note = models.CharField(max_length=200)
    deadline = models.DateTimeField(null=True)
    something = models.CharField(max_length=200, null=True)
    is_done = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
