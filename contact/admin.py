from django.contrib import admin
from .models import Contact

# Register your models here.

# admin.site.register(Contact)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'body', 'created_on')
    search_fields = ['name', 'body']
    list_filter = ('name', 'email', 'created_on')
    list_display_links = ('name',)
