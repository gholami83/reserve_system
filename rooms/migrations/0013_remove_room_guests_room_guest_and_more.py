# Generated by Django 4.2.4 on 2023-09-10 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0002_alter_guest_guest'),
        ('rooms', '0012_alter_roomchoice_room_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='guests',
        ),
        migrations.AddField(
            model_name='room',
            name='guest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='guests.guest'),
        ),
        migrations.AlterField(
            model_name='roomchoice',
            name='room_number',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
