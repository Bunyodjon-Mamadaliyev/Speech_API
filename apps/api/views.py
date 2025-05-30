from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ChatMessage, AIModel
from .serializers import ChatMessageSerializer, ChatRequestSerializer, AIModelSerializer
from .services.groq_service import GroqService


class ChatMessageViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for viewing chat messages"""
    serializer_class = ChatMessageSerializer

    def get_queryset(self):
        """Filter messages by session_id"""
        session_id = self.request.query_params.get('session_id')
        if session_id:
            return ChatMessage.objects.filter(session_id=session_id).order_by('created_at')
        return ChatMessage.objects.none()


class ChatView(APIView):
    """API view for chat interactions"""

    def post(self, request):
        """Process a chat message and return the AI response"""
        serializer = ChatRequestSerializer(data=request.data)

        if serializer.is_valid():
            session_id = serializer.validated_data.get('session_id')
            message = serializer.validated_data.get('message')
            model_id = serializer.validated_data.get('model_id')

            groq_service = GroqService()

            try:
                result = groq_service.chat_completion(
                    session_id=session_id,
                    message=message,
                    model_id=model_id
                )

                return Response({
                    'session_id': session_id,
                    'user_message': ChatMessageSerializer(result['user_message']).data,
                    'assistant_message': ChatMessageSerializer(result['assistant_message']).data,
                })

            except Exception as e:
                return Response(
                    {'error': str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AIModelViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for viewing AI models"""
    queryset = AIModel.objects.filter(is_active=True)
    serializer_class = AIModelSerializer

    @action(detail=False, methods=['get'])
    def available(self, request):
        """Get available models from Groq"""
        groq_service = GroqService()
        models = groq_service.get_available_models()

        for model_id in models:
            AIModel.objects.get_or_create(
                model_id=model_id,
                defaults={
                    'name': model_id.split('/')[-1],
                    'description': f"Groq model: {model_id}"
                }
            )

        return Response(models)