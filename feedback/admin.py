from django.contrib import admin

from .models import ContactData


@admin.register(ContactData)
class ContactDataAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'

    readonly_fields = ['name', 'email', 'subject', 'user', 'message', 'created_at', 'updated_at']

    list_display = ['name', 'email', 'subject', 'status', 'created_at']
    list_display_links = ['name', 'email', 'subject']
    list_filter = ['status', 'created_at']
