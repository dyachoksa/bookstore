from django.urls import path

from .views import add_to_cart, ShoppingCartDetailView

app_name = "store"

urlpatterns = [
    path("<int:pk>/", ShoppingCartDetailView.as_view(), name="detail"),
    path("add/<int:book_id>/", add_to_cart, name="add"),
]
