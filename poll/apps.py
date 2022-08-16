# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.apps import AppConfig


class PollConfig(AppConfig):
    """
    Class for configuring the poll app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'poll'
