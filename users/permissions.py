from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Класс проверки владельца текущего объекта.
    """
    def has_object_permission(self, request, view, obj) -> bool:
        """
        Возвращает `True` если объект принадлежит владельцу,
        если нет то `False`.
        :param request: текущий пользователь
        :param view:
        :param obj: текущий объект
        :return: bool
        """
        return obj.owner == request.user
