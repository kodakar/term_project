from django.urls import path, include

from .views import IndexView, VideoView

from . import views

urlpatterns = [
    path('', IndexView.as_view()),
    path('video', VideoView.as_view()),
    path('video_feed', views.video_feed_view(), name="video_feed"),
]
