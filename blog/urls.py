from django.urls import path, include

from .views import BlogView

urlpatterns = [
    path('', BlogView.as_view()),
]
