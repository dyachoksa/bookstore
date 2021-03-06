import os
import uuid

from django.conf import settings
from django.contrib.auth.models import User
from django.core.cache import cache
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

    @property
    def books_count(self):
        books_count = cache.get(f"{self.pk}:books-count")

        if books_count is None:
            books_count = self.books.count()
            cache.set(f"{self.pk}:books-count", books_count, timeout=3600)

        return books_count

    def get_books(self):
        return self.books.order_by('-year').all()

    def get_absolute_url(self):
        return reverse('books:author-detail', kwargs={"pk": self.pk})

    def get_photo_url(self):
        if not self.photo:
            return settings.MEDIA_URL + 'no-avatar.png'

        return self.photo.url


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
    is_featured = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Book id={self.pk} title={self.title}>"

    @property
    def in_stock(self):
        return self.store_item.in_stock

    @property
    def can_sell(self):
        return self.store_item is not None

    @property
    def avg_rating(self):
        rating = cache.get(f"{self.pk}:book-avg-rating")

        if rating is None:
            rating = round(self.reviews.aggregate(avg_rating=models.Avg("rating"))["avg_rating"] or 0, 1)
            cache.set(f"{self.pk}:book-avg-rating", rating, timeout=3600)

        return rating

    def get_all_reviews(self):
        return self.reviews.select_related('user', 'user__profile').all()

    def get_absolute_url(self):
        return reverse('books:detail', kwargs={"pk": self.pk})

    def get_cover_image_url(self):
        if not self.cover_image:
            return settings.MEDIA_URL + 'no-cover.jpeg'

        return self.cover_image.url


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    title = models.CharField(max_length=300, null=True, blank=True)
    rating = models.SmallIntegerField(default=0)
    content = models.TextField(verbose_name="Review")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "review"
        verbose_name_plural = "reviews"

    def __str__(self):
        return f"Review from {self.user} on {self.book.title}"

    def __repr__(self):
        return f"<Review id={self.pk} book_id={self.book_id} user_id={self.user_id} created_at={self.created_at}>"

    @property
    def book_title(self):
        return self.book.title

    def get_user_public_profile_url(self):
        return self.user.profile.get_absolute_url()
