# Generated by Django 4.2.4 on 2023-09-11 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_admin_user_alter_hotel_phone_alter_hotel_room'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='date_reserved',
            new_name='date_reserve',
        ),
    ]
