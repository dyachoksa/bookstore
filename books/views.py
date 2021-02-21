from django.shortcuts import render
from django.views.generic import ListView

from .models import Book


def index(request):
    books = Book.objects.all().order_by('-created_at')[:3]

    context = {
        'books': books
    }

    return render(request, "books/index.html", context=context)


class BookListView(ListView):
    model = Book
    context_object_name = "books"
