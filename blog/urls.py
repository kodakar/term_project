from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name="blog"),
    path('detail/<pk>/', views.Detail.as_view(), name="detail"),
    path('create/', views.Create.as_view(), name="create"),
    path('delete/<pk>', views.Delete.as_view(), name="delete"),
]
