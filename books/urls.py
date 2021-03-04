from django.urls import path

from .views import index, bookmark, BookListView, BookDetailView

app_name = 'books'

urlpatterns = [
    path('books/', BookListView.as_view(), name='list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('books/<int:pk>/bookmark/', bookmark, name='bookmark'),
    path('', index, name='index'),
]
