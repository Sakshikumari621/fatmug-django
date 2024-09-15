from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to="media/")
    subtitles = models.TextField(blank=True, null=True)
    processed = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Subtitle(models.Model):
    video = models.ForeignKey(
        Video, on_delete=models.CASCADE, related_name="subtitles_list"
    )
    language = models.CharField(max_length=50, default="en")
    text = models.TextField()
    start_time = models.FloatField()
    end_time = models.FloatField()

    def __str__(self):
        return f"{self.text} ({self.start_time}-{self.end_time})"
