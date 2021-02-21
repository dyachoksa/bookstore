from django.shortcuts import render

from .models import Book


def index(request):
    books = Book.objects.all().order_by('-created_at')[:3]

    context = {
        'books': books
    }

    return render(request, "books/index.html", context=context)
