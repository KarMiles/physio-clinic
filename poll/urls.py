from django.urls import path

# from . import views
from . import views as poll_views


# URL patterns for the app poll

urlpatterns = [
    path('', poll_views.home, name='poll_home'),
    path('create/', poll_views.create, name='poll_create'),
    path('results/', poll_views.results, name='poll_results'),
    path('vote/', poll_views.vote, name='poll_vote'),
]
