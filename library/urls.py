from django.urls import path

from library.apps import LibraryConfig
from library.views import (AuthorCreateAPIView, AuthorDestroyAPIView,
                           AuthorListAPIView, AuthorRetrieveAPIView,
                           AuthorUpdateAPIView, BookCreateAPIView,
                           BookDestroyAPIView, BookListAPIView,
                           BookRetrieveAPIView, BookUpdateAPIView)

app_name = LibraryConfig.name

urlpatterns = [
    path('author-create/', AuthorCreateAPIView.as_view(), name='author-create'),
    path('author-retrieve/<int:pk>/', AuthorRetrieveAPIView.as_view(), name='author-retrieve'),
    path('author-update/<int:pk>/', AuthorUpdateAPIView.as_view(), name='author-update'),
    path('author-destroy/<int:pk>/', AuthorDestroyAPIView.as_view(), name='author-destroy'),
    path('author-list/', AuthorListAPIView.as_view(), name='author-list'),

    path('book-create/', BookCreateAPIView.as_view(), name='book-create'),
    path('book-retrieve/<int:pk>/', BookRetrieveAPIView.as_view(), name='book-retrieve'),
    path('book-update/<int:pk>/', BookUpdateAPIView.as_view(), name='book-update'),
    path('book-destroy/<int:pk>/', BookDestroyAPIView.as_view(), name='book-destroy'),
    path('book-list/', BookListAPIView.as_view(), name='book-list')
]
