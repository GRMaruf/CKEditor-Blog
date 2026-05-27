from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy

def home(request):
    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'blog/home.html', {
        'posts': posts
    })


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)

    return render(request, 'blog/post_detail.html', {
        'post': post
    })

def create_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('home')

    else:
        form = PostForm()

    return render(request, 'blog/create_post.html', {
        'form': form
    })

class PostUpdateView(UpdateView):

    model = Post
    fields = ['title', 'thumbnail', 'content']
    template_name = 'blog/update_post.html'
    success_url = reverse_lazy('home')

class PostDeleteView(DeleteView):

    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home')