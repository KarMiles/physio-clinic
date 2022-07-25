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
        format = "%d/%m/%Y %H:%M"
        widgets = {
            'time': DateTimePickerInput("", format, "")
        }
