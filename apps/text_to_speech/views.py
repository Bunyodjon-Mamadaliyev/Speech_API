from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import TTS
from .serializers import TTSConvertSerializer, TTSDetailSerializer


class TTSConvertAPIView(generics.CreateAPIView):
    queryset = TTS.objects.all()
    serializer_class = TTSConvertSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.validated_data.get('text')
        voice = serializer.validated_data.get('voice')
        language = serializer.validated_data.get('language')
        speed = serializer.validated_data.get('speed')
        duration = len(text.split()) / 2
        file_size = int(duration * 150000)
        tts_instance = TTS.objects.create(
            status="completed",
            text=text,
            voice=voice,
            language=language,
            speed=speed,
            duration=duration,
            file_size=file_size,
            error="Text contains unsupported characters"
        )
        tts_instance.file_name = f"tts_{tts_instance.id}.mp3"
        tts_instance.save()
        output_serializer = self.get_serializer(tts_instance)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)


class TTSDetailAPIView(generics.RetrieveAPIView):
    queryset = TTS.objects.all()
    serializer_class = TTSDetailSerializer
    lookup_field = 'id'


class TTSAudioAPIView(APIView):
    def get(self, request, id):
        tts = get_object_or_404(TTS, pk=id)

        if tts.status != "completed":
            return Response({
                "code": "not_found",
                "message": "TTS conversion not found or audio not yet generated"
            }, status=status.HTTP_404_NOT_FOUND)
        return Response(
            tts.file_name,
            content_type='audio/mpeg',
            status=status.HTTP_200_OK
        )

class TTSHistoryAPIView(generics.ListAPIView):
    queryset = TTS.objects.all().order_by('-created_at')
    serializer_class = TTSDetailSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.query_params.get('status')
        language = self.request.query_params.get('language')
        search = self.request.query_params.get('search')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if status:
            queryset = queryset.filter(status=status)
        if language:
            queryset = queryset.filter(language=language)
        if search:
            queryset = queryset.filter(text__icontains=search)
        if start_date:
            queryset = queryset.filter(created_at__date__gte=start_date)
        if end_date:
            queryset = queryset.filter(created_at__date__lte=end_date)
        return queryset