from django.urls import path
from .views import TTSConvertAPIView

urlpatterns = [
    path('convert/', TTSConvertAPIView.as_view(), name='tts-convert'),
]
