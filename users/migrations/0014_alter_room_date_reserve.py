# Generated by Django 4.2.4 on 2023-09-12 08:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_room_date_reserve'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='date_reserve',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
