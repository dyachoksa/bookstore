from django.contrib import admin

from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']

    list_display = ['name', 'country', 'date_of_birth']
    list_filter = ['country', 'date_of_birth']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']

    readonly_fields = ['created_at']

    list_display = ['title', 'year', 'author', 'created_at']
    list_filter = ['created_at', 'year', 'author']
    list_select_related = ['author']
