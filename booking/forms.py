from django import forms
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

from .models import Booking


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = (
            'message',
            'treatment',
            'time',
            )
        widgets = {
            'time': DateTimePickerInput()
        }
