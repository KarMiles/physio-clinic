from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


# Models

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')


# Replaced by class decoration:
# admin.site.register(Post)