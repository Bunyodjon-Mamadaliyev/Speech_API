from django.urls import path
from .views import TTSConvertAPIView, TTSDetailAPIView, TTSAudioAPIView, TTSHistoryAPIView


urlpatterns = [
    path('convert/', TTSConvertAPIView.as_view(), name='tts-convert'),
    path('<int:id>/', TTSDetailAPIView.as_view(), name='tts-detail'),
    path('<int:id>/audio/', TTSAudioAPIView.as_view(), name='tts-audio'),
    path('history/', TTSHistoryAPIView.as_view(), name='tts-history'),
]
