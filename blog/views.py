
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Like
from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_list(request):
    queryset = Post.objects.filter(status="p")
    context = {
        "queryset": queryset
    }
    return render(request, "blog/post_list.html", context)

@login_required() #--> bunu url e create yazdigimda login e yönlendirmesi icin yazdim
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
    form = CommentForm()
    obj = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = obj
            comment.save()
            return redirect("blog:detail", slug=slug)
            # return redirect(request.path) -- > second way   
    context = {
        "object": obj,
        "form": form
    }
    return render(request, "blog/post_detail.html", context)

def post_update(request, slug):
    obj= get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=obj)
    if request.user.id != obj.author.id:
        return HttpResponse("You're not authorized!!")
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
    if request.user.id != obj.author.id:
        return HttpResponse("You're not authorized!!")
    if request.method=='POST':
        obj.delete()
        return redirect("blog:list")
    context = {
        "object": obj,
    }
    return render(request, "blog/post_delete.html", context)

def like(request, slug):
    if request.method == "POST":
        object = get_object_or_404(Post, slug=slug)
        like_qs = Like.objects.filter(user=request.user, post=object)
        if like_qs:
            like_qs[0].delete()
        else:
            Like.objects.create(user=request.user, post=object)
        return redirect("blog:detail", slug=slug)
    return redirect("blog:detail", slug=slug)