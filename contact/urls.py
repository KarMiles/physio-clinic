# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.urls import path
from django.views.generic import TemplateView
from django_contact_form.views import ContactFormView

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .forms import ModelContactForm


urlpatterns = [
    path(
        'contact',
        ContactFormView.as_view(
            form_class=ModelContactForm
        ),
        name='contact'),
    path(
        'contact/sent/',
        TemplateView.as_view(
            template_name='django_contact_form/contact_form_sent.html'
        ),
        name='django_contact_form_sent'),
]
