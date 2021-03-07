from django import template

from store.models import ShoppingCart, CartStatus

register = template.Library()


@register.simple_tag(takes_context=True)
def has_open_shopping_cart(context):
    request = context['request']

    if request.user.is_authenticated and ShoppingCart.objects.filter(user=request.user, status=CartStatus.NEW).exists():
        return True

    return False


@register.simple_tag(takes_context=True)
def get_shopping_cart_items_count(context):
    request = context['request']

    shopping_cart = ShoppingCart.objects\
        .filter(user=request.user, status=CartStatus.NEW)\
        .order_by("-created_at")\
        .get()

    return shopping_cart.items_count


@register.simple_tag(takes_context=True)
def get_shopping_cart(context) -> ShoppingCart:
    request = context['request']

    return ShoppingCart.objects \
        .filter(user=request.user, status=CartStatus.NEW) \
        .order_by("-created_at") \
        .get()
