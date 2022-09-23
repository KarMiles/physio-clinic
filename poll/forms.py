"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.forms import ModelForm
from django import forms

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Poll


class CreatePollForm(ModelForm):
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
