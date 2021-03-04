from django.contrib import admin

from .models import UserProfile, FavoriteBook


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["__str__", "created_at", "updated_at"]
    list_select_related = ["user"]


@admin.register(FavoriteBook)
class FavoriteBookAdmin(admin.ModelAdmin):
    list_display = ["user", "book", "created_at"]
    list_display_links = ["user", "book"]
    list_select_related = ["user", "book"]
