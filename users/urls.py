from django.urls import path

from .views import ProfileView, ProfileUpdateView, OrdersListView

app_name = 'users'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('my-orders/', OrdersListView.as_view(), name='my_orders'),
]
