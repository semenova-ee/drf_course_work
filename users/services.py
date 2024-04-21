import requests

from drf_course_work import settings


# def tg_get_updates(offset=None):
#     params = {}
#     if offset is not None:
#         params = {'offset': offset}
#     response = requests.get(f'https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/getUpdates', params=params)
#     return response.json()
#
#
# def tg_send_message(chat_id, text):
#     params = {'chat_id': chat_id, 'text': text}
#     requests.get(f'https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage', params=params)
#
class MessageToTelegram:
    def send(self, message):
        URL = 'https://api.telegram.org/bot'
        TOKEN = settings.TELEGRAM_TOKEN
        TELEGRAM_CHAT_ID = settings.TELEGRAM_CHAT_ID

        requests.post(
            url=f'{URL}{TOKEN}/sendMessage',
            data={
                'chat_id': TELEGRAM_CHAT_ID,
                'text': message
            }
        )