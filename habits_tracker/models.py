from datetime import date, datetime

from django.db import models
from django.utils import timezone
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):

    HABIT_PERIOD = [
        (1, 'Каждый день'),
        (2, 'Каждые 2 дня'),
        (3, 'Каждые 3 дня'),
        (4, 'Каждые 4 дня'),
        (5, 'Каждые 5 дней'),
        (6, 'Каждые 6 дней'),
        (7, 'Раз в неделю')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    place = models.CharField(max_length=100, verbose_name='место')
    time = models.TimeField(default=timezone.now, verbose_name='время')
    action = models.CharField(max_length=255, verbose_name='действие')
    is_good_habit = models.BooleanField(default=False, verbose_name='признак приятной привычки', **NULLABLE)
    periodic = models.PositiveSmallIntegerField(choices=HABIT_PERIOD, verbose_name='периодичность')
    lead_time = models.IntegerField(verbose_name='время выполнения', **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='публичный')
    reward = models.CharField(max_length=255, verbose_name='награда', **NULLABLE)
    associated_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='связанная привычка',
                                         **NULLABLE)
    date_last_send = models.DateField(default=datetime.today, verbose_name='дата последней отправки')

    def __str__(self):
        return f'Привычка {self.action} в {self.place} в {self.time}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
