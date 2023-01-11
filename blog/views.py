from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView

from .models import Post

class Index(ListView):
    # 一覧するモデルを指定 -> `object_list`で取得可能
    model = Post

class Detail(DetailView):
    # 詳細表示するモデルを指定 -> `object`で取得可能
    model = Post

# CreateViewは新規作成画面を簡単に作るためのView
class Create(CreateView):
    model = Post
    
    # 編集対象にするフィールド
    fields = ["title", "body"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class Delete(DeleteView):
    model = Post
    
    # 削除したあとに移動する先（トップページ）
    success_url = "/blog"