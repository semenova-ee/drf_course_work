from django.urls import path
from habits_tracker.apps import HabitsConfig
from habits_tracker.views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView, PublicHabitsAPIView


app_name = HabitsConfig.name

urlpatterns = [
    path('', HabitListAPIView.as_view(), name='list_of_habits'),
    path('create/', HabitCreateAPIView.as_view(), name='create_a_habit'),
    path('view/<int:pk>', HabitRetrieveAPIView.as_view(), name='show_habit'),
    path('edit/<int:pk>', HabitUpdateAPIView.as_view(), name='edit_habit'),
    path('delete/<int:pk>', HabitDestroyAPIView.as_view(), name='delete_habit'),
    path('public/', PublicHabitsAPIView.as_view(), name='public_habits'),
]

