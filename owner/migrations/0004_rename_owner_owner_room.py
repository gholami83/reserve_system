# Generated by Django 4.2.4 on 2023-09-10 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0003_remove_owner_owner_room_owner_guest_owner_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owner',
            new_name='room',
        ),
    ]
