from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from users.models import User


class UserTestCase(APITestCase):
    """
    Тестирование для модели привычки
    """
    def setUp(self):
        """
        Создание тестовой модели Пользователя
        :return:
        """
        self.user = User.objects.create(
            email='serious@yandex.ru',
            tg_id=503622231,
            password='12345678'
        )

    def test_user_create(self):
        """
        Тестирование создания Пользователя
        """
        data = {
            "email": "test1328@yandex.ru",
            "tg_id": 503622230,
            "password": "test1328"
        }
        response = self.client.post(
            reverse('users:user_create'),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_user_detail(self):
        """
        Тестирование для вывода информации о конкретном пользователе
        """
        retrive_url = reverse('users:user_profile', args=[self.user.pk])
        response = self.client.get(retrive_url)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        data = {
            'email': 'serious@yandex.ru',
            'tg_id': 503622231,
            'password': '12345678'
        }
        retrive_data = response.json()
        retrive_data.pop('id')
        self.assertEqual(
            retrive_data,
            data
        )

    def test_user_delete(self):
        """
        Тестирование для удаления Пользователя
        """
        delete_url = reverse('users:user_delete', args=[self.user.pk])
        response = self.client.delete(delete_url)
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            User.objects.filter(id=self.user.pk).count(),
            0
        )

    def test_user_update(self):
        """
        Тестирование для обновления информации по Пользователю
        """
        update_url = reverse('users:user_update', args=[self.user.pk])
        update_data = {
            'tg_id': 503622231
        }
        response = self.client.patch(update_url, update_data, format='json')
        self.user.refresh_from_db()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(self.user.tg_id, update_data['tg_id'])
