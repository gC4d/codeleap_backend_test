from django.db import models
from django.core.exceptions import ValidationError


class TimestampedModel(models.Model):
    """
    Abstract base model that adds common fields and validation.
    """
    username = models.CharField(max_length=255, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']

    def clean(self):
        super().clean()
        if not self.username:
            raise ValidationError({'username': 'Username is required.'})

    def save(self, *args, **kwargs):
        self.full_clean()  # Runs clean() + field validation
        super().save(*args, **kwargs)


class Post(TimestampedModel):
    """
    Represents a user-created post.
    """
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False)

    class Meta(TimestampedModel.Meta):
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['-created_at']),
        ]

    def clean(self):
        super().clean()
        if not self.title.strip():
            raise ValidationError({'title': 'Title cannot be empty or whitespace.'})

    def __str__(self):
        return f"{self.title} by {self.username}"


class Like(TimestampedModel):
    """
    Represents a like (reaction) by a user on a specific post.
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes',
    )

    class Meta(TimestampedModel.Meta):
        constraints = [
            models.UniqueConstraint(
                fields=['post', 'username'],
                name='unique_like_per_user_per_post',
            )
        ]

    def __str__(self):
        return f"{self.username} likes {self.post.title}"


class Comment(TimestampedModel):
    """
    Represents a comment left by a user on a post.
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    content = models.TextField()

    class Meta(TimestampedModel.Meta):
        indexes = [
            models.Index(fields=['post', '-created_at']),
        ]

    def clean(self):
        super().clean()
        if not self.content.strip():
            raise ValidationError({'content': 'Comment cannot be empty or whitespace.'})

    def __str__(self):
        return f"Comment by {self.username} on {self.post.title}"
