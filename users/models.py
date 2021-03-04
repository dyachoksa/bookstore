import os
import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


def get_avatar_path(instance: "UserProfile", filename: str):
    _, ext = os.path.splitext(filename)

    today = timezone.now()

    return f"users/avatars/{today.year}/{uuid.uuid4()}{ext}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(
        max_length=300, upload_to=get_avatar_path, blank=True, null=True, default="no-avatar.png"
    )
    bio = models.TextField("bio", help_text="Short information about yourself", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}' profile"

    def __repr__(self):
        return f"<UserProfile user_id={self.user_id}>"


class FavoriteBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorite_books")
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE, related_name="liked_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
