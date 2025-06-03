from rest_framework import serializers
from django.urls import reverse
from .models import TTS


class TTSConvertSerializer(serializers.ModelSerializer):
    audio_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = TTS
        fields = ["id", "status", "text", "voice", "language", "speed", "duration",
               "file_size", "audio_url", "created_at", "updated_at", "error",
        ]
        read_only_fields = ["id", "status", "duration", "file_size", "audio_url",
            "created_at", "updated_at", "error",
        ]

    def get_audio_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(
                reverse('tts-audio', args=[obj.id])
            )
        return f"https://api.example.com/api/tts/{obj.id}/audio/"

    def validate_speed(self, value):
        if not (0.25 <= value <= 4.0):
            raise serializers.ValidationError("Speed must be between 0.25 and 4.0")
        return value

    def validate_text(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Text is required and cannot be empty")
        return value


class TTSDetailSerializer(serializers.ModelSerializer):
    audio_url = serializers.SerializerMethodField()

    class Meta:
        model = TTS
        fields = [
            'id', 'status', 'text', 'voice', 'language', 'speed', 'duration',
            'file_name', 'file_size', 'created_at', 'updated_at', 'error', 'audio_url'
        ]

    def get_audio_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(f"/api/tts/{obj.id}/audio")
        return f"/api/tts/{obj.id}/audio"