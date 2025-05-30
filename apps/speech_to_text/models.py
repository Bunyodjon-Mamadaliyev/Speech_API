from django.db import models

class STT(models.Model):
    status = models.CharField(max_length=100)
    text = models.TextField()
    language = models.CharField(max_length=50)
    duration = models.FloatField(help_text="Duration in seconds")
    file_name = models.CharField(max_length=255)
    file_size = models.BigIntegerField(help_text="File size in bytes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    error = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.file_name} - {self.status}"
