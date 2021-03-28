from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Avg
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from users.models import FavoriteBook

from .forms import ReviewCreateForm
from .models import Book, Review, Author


def index(request):
    books = Book.objects.select_related('author').order_by('-created_at')[:4]
    featured_books = Book.objects.filter(is_featured=True).order_by('-created_at')
    latest_reviews = Review.objects.select_related('user', 'book').order_by('-created_at')[:5]
    most_popular_books = Book.objects.select_related('author')\
                             .annotate(rating=Avg('reviews__rating'))\
                             .filter(rating__gte=1)\
                             .order_by('-rating')[:5]

    context = {
        'books': books,
        'featured_books': featured_books,
        'latest_reviews': latest_reviews,
        'most_popular_books': most_popular_books,
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


@login_required
def remove_review(request, book_id, pk):
    book = get_object_or_404(Book, pk=book_id)

    review = book.reviews.get(pk=pk)

    if review.user != request.user:
        return HttpResponseForbidden()

    review.delete()
    messages.info(request, "You review was successfully removed.")

    return redirect(reverse("books:detail", kwargs={"pk": book.pk}))


class BookListView(ListView):
    model = Book
    context_object_name = "books"

    def get_queryset(self):
        qs = super().get_queryset().select_related('author')

        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(title__icontains=q)

        filter_by_year = self.request.GET.get('by_year')
        if filter_by_year:
            qs = qs.filter(year=filter_by_year)

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        context['q'] = self.request.GET.get('q')
        context['filter_by_year'] = int(self.request.GET.get('by_year', 0))

        context['years'] = sorted(set(Book.objects.values_list('year', flat=True)), reverse=True)

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


class AuthorListView(ListView):
    model = Author
    context_object_name = "authors"


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = "author"


class ReviewCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Review
    form_class = ReviewCreateForm
    success_message = "Thank you! Your review was successfully added."

    def get_success_url(self):
        return reverse("books:detail", kwargs={"pk": self.kwargs["pk"]})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['book'] = get_object_or_404(Book, pk=self.kwargs["pk"])

        return context

    def form_valid(self, form):
        book = get_object_or_404(Book, pk=self.kwargs["pk"])

        form.instance.book = book
        form.instance.user = self.request.user

        return super().form_valid(form)
