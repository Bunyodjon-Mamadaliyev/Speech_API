from django.db import models

class TTS(models.Model):
    status = models.CharField(max_length=100)
    text = models.TextField()
    voice = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    speed = models.FloatField(help_text="Speed factor, e.g., 1.0 = normal speed")
    duration = models.FloatField(help_text="Duration in seconds")
    file_name = models.CharField(max_length=255)
    file_size = models.BigIntegerField(help_text="File size in bytes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    error = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.file_name} - {self.status}"
