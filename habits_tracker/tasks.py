from datetime import datetime
from celery import shared_task
from habits_tracker.models import Habit
from habits_tracker.services import MessageToTelegram


@shared_task
def task_send_message():
    date_now = datetime.today().weekday()
    time_now = datetime.utcnow().time().strftime('%H:%M')

    habits = Habit.objects.filter(good_habit=False)

    for habit in habits:
        if habit.time.strftime('%H:%M') == time_now and habit.period <= date_now:
            chat_id = habit.user.tg_id
            text_message = (f"Привет, {habit.user}! Надеюсь, у тебя хороший день."
                            f"Пора заняться {habit.action} в {habit.place}")
            message = MessageToTelegram()
            message.send_habit(text=text_message, chat_id=chat_id)
