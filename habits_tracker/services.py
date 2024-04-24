from django.conf import settings
import requests


class MessageToTelegram:
    URL = 'https://api.telegram.org/bot'
    TOKEN = settings.TELEGRAM_TOKEN
    # TELEGRAM_CHAT_ID = settings.TELEGRAM_CHAT_ID

    def send_habit(self, text, chat_id):
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': chat_id,
                'text': text
            }
        )
