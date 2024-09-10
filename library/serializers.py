from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from library.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    """
    Обработка модели `Автор` для общего вида.
    """
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')


class AuthorRetrieveSerializer(serializers.ModelSerializer):
    """
    Обработка модели `Автор` для детального вида.
    """
    books = SerializerMethodField()

    def get_books(self, author) -> list[str,]:
        """
        Возвращает список книг данного автора.
        :param author: текущий автор
        :return: (list[str,]) список книг
        """
        queryset = [book.name for book in Book.objects.filter(author=author.pk)]
        return queryset

    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    """
    Обработка модели `Книга` для общего вида.
    """
    class Meta:
        model = Book
        fields = ('id', 'name', 'genre', 'status')


class BookRetrieveSerializer(serializers.ModelSerializer):
    """
    Обработка модели `Книга` для детального вида.
    """
    owner = SerializerMethodField()

    def get_owner(self, book) -> str | None:
        """
        Возвращает владельца книги если он есть, или нечего.
        :param book: текущая книга
        :return: (str | None) владелец или нечего
        """
        if book.owner:
            owner = [book.owner.email for book in Book.objects.filter(owner=book.owner.pk)]
            if owner:
                return ''.join(owner)
            return None

    class Meta:
        model = Book
        fields = '__all__'
