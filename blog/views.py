from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.
def post_list(request):
    queryset = Post.objects.all()
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