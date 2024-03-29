"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.urls import path

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from . import views


# URL patterns for the app blog

urlpatterns = [
    path("", views.PostList.as_view(), name="blog_home"),
    path("post", views.CreatePost.as_view(), name="post_create"),
    path("<slug:slug>", views.PostDetail.as_view(), name="post_detail"),
    path("<slug:slug>/delete", views.DeletePost.as_view(), name="post_delete"),
    path("<slug:slug>/edit", views.EditPost.as_view(), name="post_edit"),
    path('like/<slug:slug>', views.PostLike.as_view(), name="post_like"),
]
