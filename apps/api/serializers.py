from rest_framework import serializers
from .models import ChatMessage, AIModel


class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ['id', 'session_id', 'role', 'content', 'created_at']
        read_only_fields = ['id', 'created_at']


class ChatRequestSerializer(serializers.Serializer):
    session_id = serializers.CharField(required=False)
    message = serializers.CharField(required=True)
    model_id = serializers.CharField(required=False, default="llama-3.1-70b-versatile")

    def validate_session_id(self, value):
        if not value:
            import uuid
            return str(uuid.uuid4())
        return value


class AIModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIModel
        fields = ['id', 'name', 'model_id', 'description', 'is_active']