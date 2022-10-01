from django import forms
from .models import Post, Comment, Category


class PostForm(forms.ModelForm):
    status = forms.ChoiceField(choices=Post.OPTIONS)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select a category")
    class Meta:
        model = Post
        fields = ["title", "content",
                  "image", "category", "status"]  # '__all__'
        labels = {"category": "Category", "status": "Status"}
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
