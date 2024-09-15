from celery import shared_task
import subprocess
from .models import Video, Subtitle
from .utils import parse_subtitles


@shared_task
def process_video(video_id, language):
    video = Video.objects.get(id=video_id)
    video_file_path = video.video_file.path
    subtitles_file_path = video_file_path.replace(".mp4", ".srt")

    # Run FFmpeg to extract subtitles
    command = [
        "ffmpeg",
        "-i",
        video_file_path,
        "-map",
        "0:s:0",
        subtitles_file_path,
    ]
    subprocess.run(command, check=True)

    # Read subtitles
    with open(subtitles_file_path, "r") as file:
        subtitles_text = file.read()

    # Parse subtitles
    parsed_subtitles = parse_subtitles(subtitles_text)

    # Clear existing subtitles for the video
    Subtitle.objects.filter(video=video).delete()

    # Save parsed subtitles to the database
    for subtitle in parsed_subtitles:
        Subtitle.objects.create(
            video=video,
            language=language,
            text=subtitle["text"],
            start_time=subtitle["start_time"],
            end_time=subtitle["end_time"],
        )

    video.subtitles = subtitles_text
    video.processed = True
    video.save()
