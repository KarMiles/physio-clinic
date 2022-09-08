"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.apps import AppConfig


class ContactConfig(AppConfig):
    """
    A class for configuring the contact app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact'
