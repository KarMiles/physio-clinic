# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django import forms
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Booking
from blog.models import STATUS_LIVE, Post

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['treatment'].queryset = Post.objects.all()
        self.fields['treatment'].queryset = Post.objects.filter(status=STATUS_LIVE).order_by('title')
