# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.urls import path

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from . import views as poll_views
from . import views

# URL patterns for the app poll

urlpatterns = [
    path(
        '',
        views.PollList.as_view(),
        name='poll_home'),
    path(
        'poll',
        views.CreatePoll.as_view(),
        name='poll_create'),
    path(
        'vote/<poll_id>/',
        views.PollVote.as_view(),
        name='poll_vote'),
    path(
        'results/<poll_id>',
        views.PollResults.as_view(),
        name='poll_results'),
    path(
        'delete/<poll_id>/',
        views.DeletePoll.as_view(),
        name='poll_delete'),
]
