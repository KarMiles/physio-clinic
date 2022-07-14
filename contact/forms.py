from django import forms
from django.contrib.auth.models import User

from .models import Contact

# Forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'body',
        )


name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts")

widget=forms.TextInput(attrs={
			'type': 'text',
			'placeholder': name
			})


# SIMPLE VERSION

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = (
#             'name',
#             'email',
#             'body',
#         )
