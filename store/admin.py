from django.contrib import admin

from .models import BookItem, ShoppingCart


@admin.register(BookItem)
class BookItemAdmin(admin.ModelAdmin):
    list_display = ["book", "price", "quantity", "updated_at"]
    list_display_links = ["book", "price", "quantity"]
    list_select_related = ["book"]


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"

    list_display = ["user", "status", "total", "created_at", "updated_at"]
    list_display_links = ["user", "status"]
    list_filter = ["status", "created_at"]
    list_select_related = ["user"]
