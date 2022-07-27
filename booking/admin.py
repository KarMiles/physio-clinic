from django.contrib import admin
from .models import Booking

# Models

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        'created_on',
        'user',
        'treatment',
        'time',
        'message',
        'status',)
    search_fields = [
        'message']
    list_filter = (
        'status',
        'treatment',
        'created_on',)
    list_display_links = ('message',)
    actions = ['booking_close']

    def booking_close(self, request, queryset):
        queryset.update(status=1)
