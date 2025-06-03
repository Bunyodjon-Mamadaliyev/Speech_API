from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from apps.common.pagination import CustomPagination
from .serializers import STTSerializer
from .models import STT


class STTConvertAPIView(generics.CreateAPIView):
    queryset = STT.objects.all()
    serializer_class = STTSerializer
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        audio_file = request.FILES.get('audio')
        language = request.data.get('language')

        if not audio_file:
            return Response({
                "code": "invalid_file",
                "message": "No file provided"
            }, status=status.HTTP_400_BAD_REQUEST)
        ext = audio_file.name.split('.')[-1].lower()
        supported_formats = ['mp3', 'wav', 'm4a']

        if ext not in supported_formats:
            return Response({
                "code": "invalid_file",
                "message": "Unsupported file format",
                "details": {
                    "supported_formats": supported_formats,
                    "provided_format": ext
                }
            }, status=status.HTTP_400_BAD_REQUEST)

        if audio_file.size > 25 * 1024 * 1024:
            return Response({
                "code": "file_too_large",
                "message": "Audio file exceeds maximum size limit of 25MB"
            }, status=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)
        transcribed_text = "This is the transcribed text from the audio file."
        duration = 15.7
        stt = STT.objects.create(
            status="completed",
            text=transcribed_text,
            language=language,
            duration=duration,
            file_name=audio_file.name,
            file_size=audio_file.size,
            error="Could not process audio due to poor quality"
        )
        serializer = self.get_serializer(stt)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class STTRetrieveAPIView(generics.RetrieveAPIView):
    queryset = STT.objects.all()
    serializer_class = STTSerializer
    lookup_field = 'id'


class STTHistoryAPIView(generics.ListAPIView):
    queryset = STT.objects.all().order_by('-created_at')
    serializer_class = STTSerializer
    pagination_class = CustomPagination