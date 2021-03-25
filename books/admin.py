from django.contrib import admin

from .models import Author, Book, Review


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']

    list_display = ['name', 'country', 'date_of_birth']
    list_filter = ['country', 'date_of_birth']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']

    readonly_fields = ['created_at']

    list_display = ['title', 'year', 'author', 'is_featured', 'created_at']
    list_filter = ['is_featured', 'created_at', 'year', 'author']
    list_select_related = ['author']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    search_fields = ['content']

    readonly_fields = ["created_at", "updated_at"]

    list_display = ["book", "user", "rating", "created_at"]
    list_display_links = ["book", "user"]
    list_filter = ["created_at", "rating"]
    list_select_related = ["book", "user"]
