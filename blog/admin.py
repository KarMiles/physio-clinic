from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


# Models

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'priority', 'status', 'updated_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    list_filter = ('status', 'priority', 'updated_on', 'author')


# Replaced by class decoration:
# admin.site.register(Post)