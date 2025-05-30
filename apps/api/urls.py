from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChatMessageViewSet, ChatView, AIModelViewSet

router = DefaultRouter()
router.register(r'messages', ChatMessageViewSet, basename='chat-message')
router.register(r'models', AIModelViewSet, basename='ai-model')

urlpatterns = [
    path('', include(router.urls)),
    path('chat/', ChatView.as_view(), name='chat'),
]