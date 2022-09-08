"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django import forms
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from blog.models import STATUS_LIVE, Post
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    A class for the booking form
    """
    class Meta:  # pylint: disable=too-few-public-methods
        """
        Set fields for the form
        """
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
        """
        In booking form show only posts with status 'live'
        and order available treatments (posts) by title.
        """
        super().__init__(*args, **kwargs)
        self.fields['treatment'].queryset = Post.objects.filter(
            status=STATUS_LIVE).order_by('title')
