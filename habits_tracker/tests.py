from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from habits_tracker.models import Habit
from users.models import User

import datetime

'''HABITS TESTS'''


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='test',
            password='test123'

        )
        '''Аутентификация пользователя'''
        self.client.force_authenticate(user=self.user)

        '''Создается тестовая привычка'''
        self.habit = Habit.objects.create(
            user=self.user,
            place='Дома',
            time=datetime.time(minute=20).strftime("%Y-%m-%d %H:%M"),
            action='Делать дз',
            is_good_habit=True,
            periodic=1,
            lead_time=10,
            is_public=True
        )

    def test_create_habit(self):

        data = {
            'place': 'Кофейня',
            'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            'action': 'Купить кофе',
            'is_good_habit': False,
            'periodic': 2,
            'lead_time': 120
        }

        habit_create_url = reverse('habits:habit_create')
        response = self.client.post(habit_create_url, data=data)

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED,
        )

        self.assertEqual(
            response.json().get('action'),
            data.get('action')
        )

        self.assertTrue(
            Habit.objects.get(pk=self.habit.pk).action,
            data.get('action')
        )

    def test_list_habit(self):

        habit_list_url = reverse('habits:habit_list')

        response = self.client.get(habit_list_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            Habit.objects.get(pk=self.habit.pk).action,
            response.json().get('results')[0].get('action'))

    def test_list_habit_public(self):
        public_habit_url = reverse('habits:habit_public')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(public_habit_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), 1)

    def test_retrieve_habit(self):

        habit_one_url = reverse('habits:habit_one', args=[self.habit.pk])

        response = self.client.get(habit_one_url)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
        )

        response = response.json()

        self.assertEqual(response.get('user'), self.user.pk)
        self.assertEqual(response.get('place'), 'Дома')
        self.assertEqual(response.get('action'), 'Делать дз')

    def test_update_habit(self):

        data = {
            'place': 'updated place',
            'action': 'updated action',
        }

        habit_update_url = reverse('habits:habit_update', args=[self.habit.pk])

        response = self.client.patch(habit_update_url, data)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
        )
        response = response.json()

        self.assertEqual(response.get('place'), 'updated place')
        self.assertEqual(response.get('action'), 'updated action')

    def test_delete_habit(self):

        habit_delete_url = reverse('habits:habit_delete', args=[self.habit.pk])

        response = self.client.delete(habit_delete_url)

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT,
        )
        self.assertFalse(
            Habit.objects.all().exists(),
        )
