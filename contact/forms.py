from django import forms

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
