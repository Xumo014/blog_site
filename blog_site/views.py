from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView

# Create your views here.


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 5
    template_name = "blog/list.html"


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status='pulished', publish__year=year, publish__month=month, publish__day=day)
    return render(request, "blog/detail.html", {'post': post})

