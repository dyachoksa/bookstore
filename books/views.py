from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Book


def index(request):
    books = Book.objects.all().order_by('-created_at')[:4]

    context = {
        'books': books
    }

    return render(request, "books/index.html", context=context)


class BookListView(ListView):
    model = Book
    context_object_name = "books"

    def get_queryset(self):
        qs = super().get_queryset()

        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(title__icontains=q)

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        context['q'] = self.request.GET.get('q')

        return context


class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"
