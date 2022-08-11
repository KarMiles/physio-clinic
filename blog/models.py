# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Field choices for Post class
STATUS_LIVE = 1
STATUS_DRAFT = 0
STATUS = ((STATUS_DRAFT, "Draft"), (STATUS_LIVE, "Live"))

PRIORITY_CHOICES = [
    ("1 - Top", "Top"),
    ("2 - High", "High"),
    ("3 - Normal", "Normal"),
    ("4 - Low", "Low"),
    ("5 - Bottom", "Bottom"),
]


# Models for blog app

class Post(models.Model):
    """
    Class for the Post model
    representing a description of a treatment
    """
    title = models.CharField(
        max_length=150,
        unique=True)
    slug = models.SlugField(
        max_length=150,
        unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts")
    content = models.TextField()
    featured_image = CloudinaryField(
        'image',
        default='placeholder')
    excerpt = models.TextField(blank=True)
    price = models.CharField(
        max_length=150,
        blank=True,
        default='Please enquire at reception')
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="3 - Normal",)
    status = models.IntegerField(
        choices=STATUS,
        default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User,
        related_name='blog_likes',
        blank=True)

    class Meta:
        ordering = ['priority']

    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()
    

class Comment(models.Model):
    """Class for the Comment model
    representing comments on posts
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments')
    author = models.CharField(max_length=50)
    body = models.TextField( verbose_name=("Your comment:"),)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment by {self.author}: {self.body}"
