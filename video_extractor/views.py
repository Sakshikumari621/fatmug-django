from django.shortcuts import render, redirect
from .models import Video, Subtitle
from .forms import VideoUploadForm
from .tasks import process_video
from django.shortcuts import render, get_object_or_404


def upload_video(request):
    if request.method == "POST":
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            language = form.cleaned_data.get("language")
            video.save()
            process_video.delay(video.id, language)
            return redirect("video_list")
    else:
        form = VideoUploadForm()
    return render(request, "upload.html", {"form": form})


def video_list(request):
    videos = Video.objects.all()
    return render(request, "video_list.html", {"videos": videos})


def video_detail(request, video_id):
    video = Video.objects.get(id=video_id)
    subtitles = video.subtitles_list.all()
    return render(
        request, "video_detail.html", {"video": video, "subtitles": subtitles}
    )


def search_subtitle(request, video_id):
    query = request.GET.get("query", "")
    video = get_object_or_404(Video, id=video_id)

    subtitle = Subtitle.objects.filter(video=video, text__icontains=query)

    return render(
        request,
        "search_results.html",
        {"query": query, "subtitles": subtitle, "video": video},
    )
