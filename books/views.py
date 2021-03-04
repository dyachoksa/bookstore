from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from users.models import FavoriteBook
from .models import Book


def index(request):
    books = Book.objects.all().order_by('-created_at')[:4]

    context = {
        'books': books
    }

    return render(request, "books/index.html", context=context)


@login_required
def bookmark(request, pk):
    book = get_object_or_404(Book, pk=pk)

    try:
        favorite_book = FavoriteBook.objects.get(user=request.user, book=book)
        favorite_book.delete()
    except FavoriteBook.DoesNotExist:
        FavoriteBook.objects.create(user=request.user, book=book)

    return redirect(reverse("books:detail", kwargs={"pk": book.id}))


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['in_favourites'] = False
        if self.request.user.is_authenticated:
            context['in_favourites'] = FavoriteBook.objects.filter(user=self.request.user, book=self.object).exists()

        return context
