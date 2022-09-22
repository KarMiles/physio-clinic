"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.forms import ModelForm

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Poll


class Create PollForm(ModelForm): # TODO remove error after testing Error 500
    """
    Class for the poll form
    """
    class Meta:
        """
        Show indicated fields in the poll form
        """
        model = Poll
        fields = [
            'question',
            'option_one',
            'option_two',
            'option_three'
            ]
