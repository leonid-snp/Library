from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from library.models import Author, Book
from library.serializers import AuthorSerializer, BookSerializer


class AuthorCreateAPIView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetrieveAPIView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorUpdateAPIView(UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDestroyAPIView(DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorListAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDestroyAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
