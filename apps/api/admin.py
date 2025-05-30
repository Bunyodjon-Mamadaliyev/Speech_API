from django.contrib import admin
from .models import ChatMessage, AIModel


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('session_id', 'role', 'content_preview', 'created_at')
    list_filter = ('role', 'created_at')
    search_fields = ('session_id', 'content')

    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content

    content_preview.short_description = 'Content'


@admin.register(AIModel)
class AIModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'model_id', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'model_id')