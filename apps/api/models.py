from django.db import models


class ChatMessage(models.Model):
    """Model to store chat messages"""

    ROLE_CHOICES = (
        ('user', 'User'),
        ('assistant', 'Assistant'),
        ('system', 'System'),
    )

    session_id = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role}: {self.content[:50]}..."

    class Meta:
        ordering = ['created_at']


class AIModel(models.Model):
    """Model representing an AI model that can be used for chat"""

    name = models.CharField(max_length=100)
    model_id = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name