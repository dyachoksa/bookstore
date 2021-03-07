from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView

from books.models import Book

from .models import ShoppingCart, CartStatus


@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    shopping_cart, _ = ShoppingCart.objects \
        .filter(user=request.user, status=CartStatus.NEW) \
        .order_by("-created_at") \
        .get_or_create(defaults={"user": request.user})

    shopping_cart.books.add(book)

    return redirect(reverse("store:detail", kwargs={"pk": shopping_cart.pk}))


class ShoppingCartDetailView(LoginRequiredMixin, DetailView):
    model = ShoppingCart
    context_object_name = "shopping_cart"
