
# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django_summernote.widgets import SummernoteWidget
from django import forms

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Comment, Post


class PostForm(forms.ModelForm):
    """
    Class for blog forms
    """
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'excerpt',
            'price',
            'featured_image',
            'priority',
            'status',)
        widgets = {
            'content': SummernoteWidget()
        }


class CommentForm(forms.ModelForm):
    """
    A class for comment forms
    """
    class Meta:
        model = Comment
        fields = ('body',)
