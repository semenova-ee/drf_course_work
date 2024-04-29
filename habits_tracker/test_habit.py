from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from habits_tracker.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """
    Тестирование модели Привычки
    """

    def setUp(self):
        """
        Создание тестовой модели Пользователя (с авторизацией) и Привычки
        """
        self.user = User.objects.create(
            email='test@yandex.ru',
            password='test'
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            user=self.user,
            place="Street",
            time="21:00",
            action="Run",
            periodic=3,
            lead_time=100,
            date_last_send="2024-04-27"
        )

    def test_habit_create(self):
        """
        Тестирование создания Привычки
        """
        data = {
            "user": self.user.pk,
            "place": "Street",
            "time": "22:00",
            "action": "Run",
            "periodic": 3,
            "lead_time": 100,
            "date_last_send": "2024-04-27"
        }
        response = self.client.post(
            reverse('habits:create_a_habit'),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            Habit.objects.all().count(),
            2
        )

    def test_habit_list(self):
        """
        Тестирование вывода всех Привычек
        """
        response = self.client.get(reverse('habits:list_of_habits'))
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_habit_detail(self):
        """
        Тестирование для вывода информации о конкретной привычке
        """
        retrive_url = reverse('habits:show_habit', args=[self.habit.pk])
        response = self.client.get(retrive_url)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        data = {
            'user': self.user.id,
            'place': 'Street',
            'time': '21:00:00',
            'action': 'Run',
            'is_good_habit': False,
            'associated_habit': None,
            'periodic': 3,
            'reward': None,
            'lead_time': 100,
            'is_public': False,
            'date_last_send': "2024-04-27"
        }
        resived_data = response.json()
        resived_data.pop('id')
        self.assertEqual(
            resived_data,
            data
        )

    def test_habit_delete(self):
        """
        Тестирование для удаления Привычки
        """
        delete_url = reverse('habits:delete_habit', args=[self.habit.pk])
        response = self.client.delete(delete_url)
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Habit.objects.filter(id=self.habit.pk).count(),
            0
        )

    def test_habit_update(self):
        """
        Тестирование для обновления информации по Привычке
        """
        update_url = reverse('habits:edit_habit', args=[self.habit.pk])
        update_data = {
            'place': 'Job',
            'lead_time': 120
        }
        response = self.client.patch(update_url, update_data, format='json')
        self.habit.refresh_from_db()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(self.habit.place, update_data['place'])
        self.assertEqual(self.habit.lead_time, update_data['lead_time'])
