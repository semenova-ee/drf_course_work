from rest_framework.serializers import ValidationError


class GoodHabitValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        habit_is_good = dict(value).get('is_good_habit')  # приятная привычка
        habit_is_linked = dict(value).get('associated_habit')  # связанная привычка
        habit_reward = dict(value).get('reward')  # награда

        if habit_is_good and habit_reward is not None:
            raise ValidationError('У приятной привычки нельзя указать награду!')

        if habit_is_good and habit_is_linked is not None:
            raise ValidationError('Нельзя выбрать приятную и связанную привычки одновременно!')

        if habit_is_linked and habit_reward is not None:
            raise ValidationError('Нельзя выбрать связанную привычку и указать награду одновременно!')


class IsGoodHabitValidator:

    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        good_habit = dict(value).get(self.fields)
        if good_habit:
            if not good_habit.is_good_habit:
                raise ValidationError('Связанная привычка может быть только с признаком приятной привычки!')


class TimeHabitValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        lead_time = dict(value).get(self.field)
        if int(lead_time) > 120:
            raise ValidationError('Время выполнения не должно превышать 120 сек!')


class PeriodicHabitValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if int(tmp_val) > 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')
        date_last_send = dict(value).get('date_last_send')
        if date_last_send is None:
            raise ValidationError('Нельзя оставить date_last_send пустым. '
                                  'Если ты только создаешь привычку, поставь текущую дату. '
                                  'Напоминание придет в заданный период')
