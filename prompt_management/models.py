from django.db import models
from django.db.models import CharField
import uuid


class Prompt(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title: str = models.CharField(max_length=255)
    content: str = models.TextField()

    def __str__(self):
        return str(self.title)
