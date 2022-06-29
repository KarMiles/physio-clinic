from django.contrib import admin
from .models import Booking

# Models

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('updated_on', 'user', 'treatment', 'time', 'message')
    search_fields = ['user', 'treatment', 'message']
    list_filter = ('treatment', 'updated_on')
    list_display_links = ('message',)
