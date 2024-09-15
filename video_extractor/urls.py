# from django.urls import path
# from . import views

# urlpatterns = [
#     path("upload/", views.upload_video, name="upload_video"),
#     path("videos/", views.video_list, name="video_list"),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.upload_video, name="upload_video"),
    path("videos/", views.video_list, name="video_list"),
    path("videos/<int:video_id>/", views.video_detail, name="video_detail"),
    path(
        "videos/<int:video_id>/search/", views.search_subtitle, name="search_subtitle"
    ),
]
