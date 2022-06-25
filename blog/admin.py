from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


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

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('author', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)