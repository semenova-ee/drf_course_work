from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class User(AbstractUser):

    username = None

    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    tg_id = models.IntegerField(unique=True, verbose_name='ID телеграме', default=None, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
