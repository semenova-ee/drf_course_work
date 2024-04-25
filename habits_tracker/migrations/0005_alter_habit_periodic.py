# Generated by Django 5.0.4 on 2024-04-25 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits_tracker', '0004_alter_habit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='periodic',
            field=models.CharField(choices=[('1', 'Раз в неделю'), ('2', 'Два раза в неделю'), ('3', 'Три раза в неделю'), ('4', 'Четыре раза в неделю'), ('5', 'Пять раз в неделю'), ('6', 'Шесть раз в неделю'), ('7', 'Семь раз в неделю')], max_length=20, verbose_name='периодичность'),
        ),
    ]
