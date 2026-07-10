from django import forms
from .models import Comment

class BlogPostCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "nickname",
            "email",
            "address",
            "city",
            "province",
            "hide_name",
            "comment",
        ]