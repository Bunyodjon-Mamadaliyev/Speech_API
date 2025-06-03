from rest_framework import serializers
from .models import STT

class STTSerializer(serializers.ModelSerializer):
    audio = serializers.FileField(write_only=True)

    class Meta:
        model = STT
        fields = ["id", "status", "text", "language", "duration", "file_name", "file_size",
            "created_at", "updated_at", "error", "audio",
        ]
        read_only_fields = [
            "id", "status", "text", "duration", "file_name", "file_size",
            "created_at", "updated_at", "error"
        ]
