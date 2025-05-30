from django.urls import path
from .views import STTConvertAPIView, STTRetrieveAPIView, STTHistoryAPIView

urlpatterns = [
    path('convert/', STTConvertAPIView.as_view(), name='stt-convert'),
    path('<int:id>/', STTRetrieveAPIView.as_view(), name='stt-retrieve'),
    path('history/', STTHistoryAPIView.as_view(), name='stt-history'),
]
