from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import F
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views.generic import DetailView, TemplateView

from books.models import Book

from .models import ShoppingCart, CartStatus, BookItem


@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    shopping_cart, _ = ShoppingCart.objects \
        .filter(user=request.user, status=CartStatus.NEW) \
        .order_by("-created_at") \
        .get_or_create(defaults={"user": request.user})

    shopping_cart.books.add(book)

    return redirect(reverse("store:detail", kwargs={"pk": shopping_cart.pk}))


@login_required
def remove_from_cart(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    shopping_cart = ShoppingCart.objects \
        .filter(user=request.user, status=CartStatus.NEW) \
        .order_by("-created_at") \
        .get()

    shopping_cart.books.remove(book)

    if shopping_cart.books.count():
        messages.success(request, f"{book.title} was removed from your cart.")
        return redirect(reverse("store:detail", kwargs={"pk": shopping_cart.pk}))

    shopping_cart.delete()
    messages.info(request, "Your cart was cleared. See you soon!")

    return redirect(reverse("books:list"))


@login_required
@require_POST
def purchase(request, pk):
    shopping_cart = get_object_or_404(ShoppingCart, pk=pk)

    if shopping_cart.user.pk != request.user.pk:
        return HttpResponseForbidden()

    # Do actual card charge here
    # using request.POST data
    # ...

    shopping_cart.status = CartStatus.COMPLETED
    shopping_cart.save()

    BookItem.objects \
        .filter(book_id__in=shopping_cart.books.all()) \
        .update(quantity=F("quantity") - 1)

    return redirect(reverse("store:purchase_success", kwargs={"pk": shopping_cart.pk}))


class ShoppingCartDetailView(LoginRequiredMixin, DetailView):
    model = ShoppingCart
    context_object_name = "shopping_cart"


class ShoppingCartSuccessView(LoginRequiredMixin, TemplateView):
    template_name = "store/shoppingcart_success.html"
