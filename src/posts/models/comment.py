from django.db import models
from django.core.exceptions import ValidationError
from .base import TimestampedModel
from .post import Post


class Comment(TimestampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    username = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['-created_datetime']

    def clean(self):
        super().clean()
        if not self.content:
            raise ValidationError('Content is required')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Comment by {self.username} on {self.post.title}"
