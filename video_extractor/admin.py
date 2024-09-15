from django.contrib import admin
from .models import Video, Subtitle


class SubtitleInline(admin.TabularInline):
    model = Subtitle
    extra = 1  # Number of blank subtitle forms to display


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "processed", "uploaded_at")
    inlines = [SubtitleInline]


@admin.register(Subtitle)
class SubtitleAdmin(admin.ModelAdmin):
    list_display = ("video", "text", "start_time", "end_time")
