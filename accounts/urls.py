from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/<username>', views.ProfileView.as_view(), name='profile'),
    path('myDetail/<pk>/', views.myDetail.as_view(), name="myDetail"),
]
