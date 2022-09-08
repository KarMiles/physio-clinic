"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.forms import ModelForm

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Poll


class CreatePollForm(ModelForm):
    """
    Class for the poll form
    """
    class Meta:
        model = Poll
        fields = [
            'question',
            'option_one',
            'option_two',
            'option_three'
            ]
