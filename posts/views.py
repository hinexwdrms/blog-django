from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'posts/home.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm() # if get request
    return render(request, 'posts/create_post.html', {'form':form})

def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author: #check if logged in user is author
        return redirect('home')
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post) 
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post) #instance tells to update the existing form instead of creating
    return render(request, 'posts/edit_post.html', {'form': form})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return redirect('home')
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'posts/delete_post.html', {'post': post})