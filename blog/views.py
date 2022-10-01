from django.shortcuts import render
from .models import Post
# Create your views here.
def post_list(request):
    queryset = Post.objects.all()
    context = {
        "queryset": queryset
    }
    return render(request, "blog/post_list.html", context)