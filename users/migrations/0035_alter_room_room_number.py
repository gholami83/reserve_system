# Generated by Django 4.2.4 on 2023-09-20 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0034_room_until_reserve'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_number',
            field=models.IntegerField(),
        ),
    ]
