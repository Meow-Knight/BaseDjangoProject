from django.db import models
from django.db.models import Manager
from django.utils import timezone
import uuid


class TimeStampedModel(models.Model):
    objects = Manager
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
