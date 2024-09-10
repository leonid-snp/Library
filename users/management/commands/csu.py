from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Класс для запуска команды создания суперпользователя.
    """
    def handle(self, *args, **kwargs) -> None:
        """
        Создает суперпользователя.
        :param args:
        :param kwargs:
        :return: None
        """
        user = User.objects.create(
            email='admin@admin.com',
        )
        user.set_password('12345')
        user.is_staff = True
        user.is_superuser = True
        user.save()
