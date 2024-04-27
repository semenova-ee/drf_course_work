from rest_framework import serializers
from habits_tracker.models import Habit
from habits_tracker.validators import TimeHabitValidator, IsGoodHabitValidator, PeriodicHabitValidator, GoodHabitValidator


# class PleasureHabitSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Habit
#         fields = ('user', 'place', 'time', 'action', 'periodic', 'lead_time', 'is_public', 'associated_habit',)


class HabitSerializer(serializers.ModelSerializer):

    # pleasant_habit = PleasureHabitSerializer(source='habit_set.all', many=True)

    class Meta:
        model = Habit
        fields = '__all__'


class HabitCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = ('id', 'user', 'place', 'time', 'action', 'periodic', 'is_public', 'lead_time', 'associated_habit',
                  'is_good_habit', 'reward', 'date_last_send')
        validators = [GoodHabitValidator(fields),
                      IsGoodHabitValidator(fields='associated_habit'),
                      TimeHabitValidator(field='lead_time'),
                      PeriodicHabitValidator(field='periodic')]
