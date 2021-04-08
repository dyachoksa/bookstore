from django.contrib.sitemaps import Sitemap

from .models import Author, Book


class BooksSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return Book.objects.order_by('-created_at')

    def lastmod(self, obj: Book):
        return obj.updated_at


class AuthorsSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return Author.objects.all()
