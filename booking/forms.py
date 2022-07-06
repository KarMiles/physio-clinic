from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    time = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(format='%d/%m/%Y %H:%M')
    )

    class Meta:
        model = Booking
        fields = (
            'message',
            'treatment',
            'time',
            )
