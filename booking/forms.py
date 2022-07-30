# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django import forms
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    A class for booking forms
    """
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
