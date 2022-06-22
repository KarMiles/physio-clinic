from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Live"))

class Priority(models.Model):

    class Level(models.IntegerChoices):
        TOP = 1
        HIGH = 2
        NORMAL = 3
        LOW = 4
        BOTTOM = 5

    level = models.IntegerField(choices=Level.choices, default=3)

# Models

class Post(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    priority = Priority.level
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    
    class Meta:
        ordering = ['priority']
    
    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()
    

