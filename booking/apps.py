"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.apps import AppConfig


class BookingConfig(AppConfig):
    """
    Class for configuring the booking app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking'
