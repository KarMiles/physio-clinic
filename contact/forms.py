from django import forms
from django.contrib.auth.models import User
from django_contact_form.forms import ContactForm

from .models import Contact


# Forms

class ModelContactForm(ContactForm):

    def __init__(
        self,
        data=None,
        files=None,
        request=None,
        recipient_list=None,
        *args,
        **kwargs):
        if request is not None and request.method == 'GET' and request.user.is_authenticated:
            kwargs['initial'] = {
                'email': request.user.email,
                'name': request.user.get_full_name() or request.user.username
            }
        super().__init__(data, files, request, recipient_list, *args, **kwargs)

    def save(self, fail_silently=False):
        data = self.get_message_dict()
        print(data)
        Contact.objects.create(
            name=self.cleaned_data.get("name"),
            email=self.cleaned_data.get("email"),
            subject=data['subject'],
            body=data['message'])
        # Uncomment when email functionality operational:
        super().save(fail_silently=False)
