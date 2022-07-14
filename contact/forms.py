from django import forms
from django.contrib.auth.models import User
from django_contact_form.forms import ContactForm

from .models import Contact


# Forms

class ModelContactForm(ContactForm):

    def save(self, fail_silently=False):
        data = self.get_message_dict()
        Contact.objects.create(
            name=self.cleaned_data.get("name"),
            from_email=data['from_email'],
            subject=data['subject'],
            body=data['message'])
        # Uncomment when email functionality operational:
        super().save(fail_silently=False)


# name = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name="blog_posts")

# widget=forms.TextInput(attrs={
# 			'type': 'text',
# 			'placeholder': name
# 			})


# SIMPLE VERSION

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = (
#             'name',
#             'email',
#             'body',
#         )
