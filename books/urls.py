from django.urls import path

from .views import index, BookListView, BookDetailView

app_name = 'books'

urlpatterns = [
    path('books/', BookListView.as_view(), name='list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('', index, name='index'),
]
