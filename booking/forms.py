from django import forms
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

from .models import Booking


class BookingForm(forms.ModelForm):
    
    # time = forms.DateTimeField(
    #     input_formats=['%d/%m/%Y %H:%M'],
    #     widget=forms.DateTimeInput(format='%d/%m/%Y %H:%M'),
    #     initial='DD/MM/YYYY hh:mm'
    # )

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
