# Generated by Django 5.0.4 on 2024-04-27 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits_tracker', '0009_alter_habit_date_last_send'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='periodic',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Каждый день'), (2, 'Каждые 2 дня'), (3, 'Каждые 3 дня'), (4, 'Каждые 4 дня'), (5, 'Каждые 5 дней'), (6, 'Каждые 6 дней'), (7, 'Раз в неделю')], verbose_name='периодичность'),
        ),
    ]
