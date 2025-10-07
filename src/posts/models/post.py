from django.db import models
from .base import TimestampedModel


class Post(TimestampedModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    username = models.CharField(max_length=255)

    class Meta:
        ordering = ['-created_datetime']

    def __str__(self):
        return self.title
