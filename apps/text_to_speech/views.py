from rest_framework import generics, status
from rest_framework.response import Response
from .models import TTS
from .serializers import TTSConvertSerializer

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
