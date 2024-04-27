from datetime import datetime, date, timedelta
from celery import shared_task
from habits_tracker.models import Habit
from habits_tracker.services import MessageToTelegram


@shared_task
def task_send_message():
    # date_now = datetime.today().weekday()
    # time_now = datetime.utcnow().time().strftime('%H:%M')
    # date_today = datetime.today()

    habits = Habit.objects.filter(is_good_habit=False)

    for habit in habits:
        rate = int(habit.periodic) #получаем значение периодичности
        time_now = datetime.utcnow().time().strftime('%H:%M') #получаем текущее время
        date_today = datetime.today().date() #получаем текущую дату
        days_since_last_send = (datetime.today().date()-habit.date_last_send).days #находим разницу между текущим днем и днем отправки, получаем кол-во дней


        if habit.time.strftime('%H:%M') <= time_now and days_since_last_send == rate:
            #если количество дней между текущей датой и предыдущей отправкой равно периодичности
            #выполнения хобби, то сообщение будет отправлено в указаное время

            chat_id = habit.user.tg_id
            text_message = (f"Привет, {habit.user.first_name}! Надеюсь, у тебя хороший день. "
                            f"\nТы создал привычку {habit.action} в {habit.place}. "
                            f"\nЕе нужно выполнять с периодичностью: каждые {habit.periodic} дня. "
                            f"\nСделай это сегодня!")
            if habit.reward :
                text_message += f"\n А в подарок можешь позволнить себе {habit.reward}"
            message = MessageToTelegram()
            message.send_habit(text=text_message,chat_id=chat_id)
            habit.date_last_send = date_today
            habit.save()


