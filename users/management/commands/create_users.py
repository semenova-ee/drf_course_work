from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        for obj in range(3):
            user = User.objects.create(
                email=f'user{obj}@user.com',
                first_name=f'user{obj}',
                is_active=True,
            )
            user.set_password('123')
            user.save()
            print(f'Созданы тестовые пользователи:\n'
                  f'Пользователь: {user.email}, пароль: 1\n')
