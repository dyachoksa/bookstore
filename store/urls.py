from django.urls import path

from .views import add_to_cart, remove_from_cart, purchase, ShoppingCartDetailView, ShoppingCartSuccessView

app_name = "store"

urlpatterns = [
    path("<int:pk>/", ShoppingCartDetailView.as_view(), name="detail"),
    path("<int:pk>/purchase/", purchase, name="purchase"),
    path("<int:pk>/purchase/success/", ShoppingCartSuccessView.as_view(), name="purchase_success"),
    path("add/<int:book_id>/", add_to_cart, name="add"),
    path("remove/<int:book_id>/", remove_from_cart, name="remove"),
]
