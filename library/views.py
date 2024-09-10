from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated

from library.models import Author, Book
from library.serializers import (AuthorRetrieveSerializer, AuthorSerializer,
                                 BookRetrieveSerializer, BookSerializer)
from users.permissions import IsOwner


class AuthorCreateAPIView(CreateAPIView):
    """
    Класс представления создания Автора.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetrieveAPIView(RetrieveAPIView):
    """
    Класс представления просмотра Автора.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorRetrieveSerializer


class AuthorUpdateAPIView(UpdateAPIView):
    """
    Класс представления редактирования Автора.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDestroyAPIView(DestroyAPIView):
    """
    Класс представления удаления Автора.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorListAPIView(ListAPIView):
    """
    Класс представления просмотра списка Авторов.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookCreateAPIView(CreateAPIView):
    """
    Класс представления создания Книги.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveAPIView(RetrieveAPIView):
    """
    Класс представления просмотра книги.
    """
    queryset = Book.objects.all()
    serializer_class = BookRetrieveSerializer


class BookUpdateAPIView(UpdateAPIView):
    """
    Класс представления редактирования Книги.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsOwner | IsAuthenticated,)

    def perform_update(self, serializer) -> None:
        """
        Проверяет статус книги, если книга выдана,
        прикрепляет текущего пользователя как владельца книги.
        :param serializer: текущая книга
        :return: None
        """
        book = serializer.save()
        user = self.request.user
        if book.status == 'Issued':
            book.owner = user
            book.save()
        else:
            book.owner = None
            book.save()


class BookDestroyAPIView(DestroyAPIView):
    """
    Класс представления удаления Книги.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListAPIView(ListAPIView):
    """
    Класс представления просмотра списка Книг.

    Отображает книги только со статусом `В наличии`,
    или книги текущего пользователя.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'author', 'genre']

    def get_queryset(self) -> list[object,]:
        """
        Проверяет статус книги и принадлежность к текущему пользователю,
        если хоть одно условие совпадет, отображает эту книгу.
        :return:
        """
        user = self.request.user
        queryset = self.queryset
        return queryset.filter(Q(status='In_stock') | Q(owner=user.pk))
