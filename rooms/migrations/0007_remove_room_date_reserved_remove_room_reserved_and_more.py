# Generated by Django 4.2.4 on 2023-09-09 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_alter_room_choice_room_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='date_reserved',
        ),
        migrations.RemoveField(
            model_name='room',
            name='reserved',
        ),
        migrations.AlterField(
            model_name='room',
            name='choice_room_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.roomchoice'),
        ),
    ]
