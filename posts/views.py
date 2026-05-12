from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all()
    return HttpResponse(f"Total posts: {posts.count()}")

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return HttpResponse(f"Post: {post.title}")