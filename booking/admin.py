# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Booking


# Models for booking app in admin page

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin class for the booking model
    """
    list_display = (
        'created_on',
        'user',
        'treatment',
        'time',
        'message',
        'status',)
    search_fields = [
        'user',
        'message']
    list_filter = (
        'status',
        'created_on',
        'user',
        'treatment',)
    list_display_links = ('message',)
    actions = ['booking_close']

    def booking_close(self, request, queryset):
        queryset.update(status=1)
