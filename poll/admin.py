# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Poll


# Models for poll app

@admin.register(Poll)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin class for the poll model.
    """
    list_display = ('question',)
    list_filter = ('question',)
    list_display_links = ('question',)
