from django.db import models
from django.core.exceptions import ValidationError


class TimestampedModel(models.Model):
    """Base model with common fields for all models"""  
    created_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def clean(self):
        if not self.username:
            raise ValidationError('Username is required')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
