from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from library.models import Book
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Обработка модели `Пользователь` для общего вида.
    """
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')


class UserRetrieveSerializer(serializers.ModelSerializer):
    """
    Обработка модели `Пользователь` для детального просмотра.
    """
    books = SerializerMethodField()

    def get_books(self, user) -> list[str,]:
        """
        Возвращает список книг данного пользователя.
        :param user: текущий пользователь
        :return: (list[str,]) список книг
        """
        return [book.name for book in Book.objects.filter(owner=user.pk)]

    class Meta:
        model = User
        fields = '__all__'
