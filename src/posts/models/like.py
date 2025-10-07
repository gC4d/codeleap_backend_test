from django.db import models
from django.core.exceptions import ValidationError
from .base import TimestampedModel
from .post import Post


class Like(TimestampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    username = models.CharField(max_length=255)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['post', 'username'],
                name='unique_like_per_user_per_post',
                violation_error_code='LIKE_ALREADY_EXISTS',
                violation_error_message='You have already liked this post.'
            )
        ]
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} likes {self.post.title}"
