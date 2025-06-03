from django.contrib import admin
from .models import TTS

@admin.register(TTS)
class TTSAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'file_name', 'status', 'voice', 'language', 'speed',
        'duration', 'file_size', 'created_at', 'updated_at'
    )
    list_filter = ('status', 'language', 'voice', 'created_at')
    search_fields = ('file_name', 'text', 'error')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': (
                'status', 'text', 'voice', 'language', 'speed',
                'duration', 'file_name', 'file_size', 'error'
            )
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
