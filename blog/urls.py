from django.urls import path
from . import views


# URL patterns for the app blog

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("post", views.CreatePost.as_view(), name="post_create"),
    path("<slug:slug>", views.PostDetail.as_view(), name="post_detail"),
    path("<slug:slug>/edit", views.EditPost.as_view(), name="post_edit"),
    path('like/<slug:slug>', views.PostLike.as_view(), name="post_like"),
]
