from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from users.models import User
from users.serializers import UserRetrieveSerializer, UserSerializer


class UserCreateAPIView(CreateAPIView):
    """
    Класс представления создания Пользователя.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer) -> None:
        """
        Шифрует пароль пользователя.
        :param serializer: текущий пользователь
        :return: None
        """
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserRetrieveAPIView(RetrieveAPIView):
    """
    Класс представления просмотра Пользователя.
    """
    queryset = User.objects.all()
    serializer_class = UserRetrieveSerializer


class UserUpdateAPIView(UpdateAPIView):
    """
    Класс представления редактирования Пользователя.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_update(self, serializer):
        """
        Шифрует пароль пользователя.
        :param serializer: текущий пользователь
        :return: None
        """
        user = serializer.save()
        user.set_password(user.password)
        user.save()


class UserDestroyAPIView(DestroyAPIView):
    """
    Класс представления удаления Пользователя.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListAPIView(ListAPIView):
    """
    Класс представления просмотра списка Пользователей.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
