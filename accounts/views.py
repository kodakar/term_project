from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView

from blog.models import Post


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class ProfileView(ListView):
    template_name = 'accounts/profiel.html'
    model = Post

class myDetail(DetailView):
    # 詳細表示するモデルを指定 -> `object`で取得可能
    template_name = 'accounts/myPost_detail.html'
    model = Post


