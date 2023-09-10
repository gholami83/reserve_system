# Generated by Django 4.2.4 on 2023-09-10 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0013_remove_room_guests_room_guest_and_more'),
        ('guests', '0002_alter_guest_guest'),
        ('owner', '0004_rename_owner_owner_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='guest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='guests.guest'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rooms.room'),
        ),
    ]
