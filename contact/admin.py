# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Contact

# Admin model for contact app


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin class for the contact model.
    """
    list_display = ('name', 'email', 'body', 'created_on')
    search_fields = ['name', 'body']
    list_filter = ('name', 'email', 'created_on')
    list_display_links = ('body',)
