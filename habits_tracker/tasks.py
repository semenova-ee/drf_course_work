from datetime import datetime
from celery import shared_task
from habits_tracker.models import Habit
from habits_tracker.services import MessageToTelegram


@shared_task
def task_send_message():
    date_now = datetime.today().weekday()
    time_now = datetime.utcnow().time().strftime('%H:%M')

    habits = Habit.objects.filter(is_good_habit=False)
    # habits = Habit.objects.all()

    for habit in habits:
        # habit.time = time_now
        # habit.save()
        if habit.time.strftime('%H:%M') <= time_now and int(habit.periodic) >= date_now:
            chat_id = habit.user.tg_id
            text_message = (f"Привет, {habit.user}! Надеюсь, у тебя хороший день."
                            f"Ты создал привычку {habit.action} в {habit.place}."
                            f"Ее нужно выполнять с периодичностью {habit.periodic} раз в неделю.")
            if habit.reward:
                text_message += f"\nА в подарок можешь позволнить себе {habit.reward}"
            message = MessageToTelegram()
            message.send_habit(text=text_message,chat_id=chat_id)


