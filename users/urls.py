from django.urls import path

from .views import PublicProfileView, ProfileView, ProfileUpdateView, UserUpdateView, OrdersListView

app_name = 'users'

urlpatterns = [
    path('<int:pk>/', PublicProfileView.as_view(), name="public"),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('user/edit/', UserUpdateView.as_view(), name='user_edit'),
    path('my-orders/', OrdersListView.as_view(), name='my_orders'),
]
