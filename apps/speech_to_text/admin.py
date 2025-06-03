from django.contrib import admin
from .models import STT

@admin.register(STT)
class STTAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_name', 'status', 'language', 'duration', 'file_size', 'created_at', 'updated_at')
    list_filter = ('status', 'language', 'created_at')
    search_fields = ('file_name', 'text', 'error')
    readonly_fields = ('created_at', 'updated_at')
