from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.
def post_list(request):
    queryset = Post.objects.filter(status="p")
    context = {
        "queryset": queryset
    }
    return render(request, "blog/post_list.html", context)

def post_create(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("blog:list")
    context = {
        "form": form
    }
    return render(request, "blog/post_create.html", context)

def post_detail(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    context = {
        "object": obj
    }
    return render(request, "blog/post_detail.html", context)

def post_update(request, slug):
    obj= get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("blog:list")
    context = {
        "object": obj,
        "form": form
    }
    return render(request, "blog/post_update.html", context)

def post_delete(request, slug):
    obj= get_object_or_404(Post, slug=slug)
    if request.method=='POST':
        obj.delete()
        return redirect("blog:list")
    context = {
        "object": obj,
    }
    return render(request, "blog/post_delete.html", context)