from django.urls import path

from .views import index, BookListView

app_name = 'books'

urlpatterns = [
    path('books/', BookListView.as_view(), name='list'),
    path('', index, name='index'),
]
