# Generated by Django 5.0.4 on 2024-04-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='telegram',
        ),
        migrations.AddField(
            model_name='user',
            name='tg_id',
            field=models.IntegerField(default=None, null=True, unique=True, verbose_name='ID телеграме'),
        ),
    ]
