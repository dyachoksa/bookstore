from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy

from .models import Book


class BooksFeed(Feed):
    title = "Latest books"
    link = reverse_lazy('books:list')
    description = "A collection of our latest additions to the bookstore"

    def items(self):
        return Book.objects.order_by('-created_at')[:3]

    def item_title(self, item: Book):
        return item.title

    def item_description(self, item: Book):
        return item.description
