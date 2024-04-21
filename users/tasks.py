import datetime

from celery import shared_task
from django.utils import timezone

from habits_tracker.models import Habit
from habits_tracker.services import MessageToTelegram
from users.models import User


# @shared_task
# def telegram_bot_updates():
#     tg_data = tg_get_updates()
#     users = User.objects.filter(is_active=False)
#     print(1)
#     if tg_data['ok'] and tg_data['result'] != []:
#         for message in tg_data['result']:
#             print(message)
#             if message['message']['text'] == "/start":
#                 for user_one in users:
#                     if user_one.username.lower() == message['message']['from']['username'].lower():
#                         user_one.telegram = message['message']['from']['id']
#                         user_one.first_name = message['message']['from']['first_name']
#                         user_one.is_active = True
#                         user_one.save()
#                         tg_get_updates(message['update_id'])
#                         text = f'Ваша учетная запись активирована.'
#                         tg_send_message(message['message']['from']['id'], text)
#             tg_get_updates(message['update_id'])

@shared_task
def habits_worker():
    now = datetime.datetime.now()
    now = timezone.make_aware(now, timezone.get_current_timezone())
    now += datetime.timedelta(minutes=10)
    habits = Habit.objects.all()
    reminder = MessageToTelegram()

    for habit in habits:
        message = f"В {habit.time.strftime('%H:%M')} я буду {habit.action} в {habit.location}"
        if not habit.is_nice_habit and now.hour == habit.time.hour and now.minute == habit.time.minute:
            reminder.send(message)