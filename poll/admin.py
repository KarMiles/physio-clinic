from django.contrib import admin

from .models import Poll


# Models for poll app

@admin.register(Poll)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('question',)
    list_filter = ('question',)
    list_display_links = ('question',)
