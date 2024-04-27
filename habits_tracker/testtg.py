from datetime import datetime

import requests


URL = 'https://api.telegram.org/bot'
TOKEN = '7018773631:AAFJHHsBJ09blFTIrsKfYxdXmwksTELnvpc'
# TELEGRAM_CHAT_ID = settings.TELEGRAM_CHAT_ID

def send_habit():
    requests.post(
        url=f'{URL}{TOKEN}/sendMessage',
        data={
            'chat_id': 503622235,
            'text': '27 апреля 2024 г. тест бота'
        }
    )

# send_habit()

print(datetime.utcnow().time().strftime('%H:%M'))
print(str(datetime.today().weekday()))
print(type(datetime.today()))
print(type(datetime.today().date()))


