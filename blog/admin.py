# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Post, Comment


# Models for blog management in admin page

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin class for the blog model.
    Section for managing posts.
    """
    list_display = ('title', 'priority', 'status', 'updated_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    list_filter = ('status', 'priority', 'updated_on', 'author')

# Decoration replaces class:
# admin.site.register(Post)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin class for the blog model.
    Section for managing comments.
    """
    list_display = ('author', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    list_display_links = ('body',)
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        Approve comments
        """
        queryset.update(approved=True)
