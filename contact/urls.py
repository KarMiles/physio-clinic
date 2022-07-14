from django.urls import include, path
from django.views.generic import TemplateView

from django_contact_form.views import ContactFormView

from .forms import ContactForm


# URL patterns for the app contact

# urlpatterns = [
#     path('', TemplateView.as_view(template_name='contact.html'), name='contact'),
# ]

urlpatterns = [
    path(
        'contact',
        ContactFormView.as_view(
            form_class=ContactForm
        ),
        name='django_contact_form'),
    path(
        'contact/sent/',
        TemplateView.as_view(
            template_name='django_contact_form/contact_form_sent.html'
        ),
        name='django_contact_form_sent'),
]
