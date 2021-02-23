import os
import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=300)
    country = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    photo = models.ImageField(max_length=300, upload_to='authors/%Y', blank=True, null=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Author id={self.pk} name={self.name}>"


def get_image_path(instance: "Book", filename: str):
    _, ext = os.path.splitext(filename)

    today = timezone.now()

    return f"books/covers/{today.year}/{uuid.uuid4()}{ext}"


class Book(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    cover_image = models.ImageField(max_length=300, upload_to=get_image_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Book id={self.pk} title={self.title}>"

    def get_absolute_url(self):
        return reverse('books:detail', kwargs={"pk": self.pk})

    def get_cover_image_url(self):
        if not self.cover_image:
            return settings.MEDIA_URL + 'no-cover.jpeg'

        return self.cover_image.url
