from django import forms
from .models import Video


class VideoUploadForm(forms.ModelForm):
    language = forms.CharField(
        max_length=50,
        label="Subtitle Language",
        help_text="Enter the language code (e.g., 'en' for English)",
    )

    class Meta:
        model = Video
        fields = ["title", "video_file", "language"]
