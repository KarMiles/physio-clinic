from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = (
            'message',
            'user',
            'treatment',
            'time',
            'email',
            )
