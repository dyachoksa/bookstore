from django.urls import path

from .views import (
    index, bookmark, remove_review,

    BookListView, BookDetailView,

    ReviewCreateView,

    AuthorListView, AuthorDetailView
)

app_name = 'books'

urlpatterns = [
    path('books/', BookListView.as_view(), name='list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('books/<int:pk>/bookmark/', bookmark, name='bookmark'),
    path('books/<int:pk>/reviews/', ReviewCreateView.as_view(), name='review-create'),
    path('books/<int:book_id>/reviews/<int:pk>/remove/', remove_review, name='review-remove'),

    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),

    path('', index, name='index'),
]
