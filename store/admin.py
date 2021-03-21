from django.contrib import admin

from .models import BookItem, ShoppingCart, ShippingAddress


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


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    search_fields = ["country", "city", "address_line", "zip_code"]

    list_display = ["__str__", "user", "is_default"]
    list_display_links = ["__str__"]
    list_filter = ["is_default"]
    list_select_related = ["user"]
