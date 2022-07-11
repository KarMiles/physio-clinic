from django.urls import path
from . import views
from django.views.generic import TemplateView


# URL patterns for the app contact

urlpatterns = [
    path('', TemplateView.as_view(template_name='contact.html'), name='contact'),
]
