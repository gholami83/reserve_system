# Generated by Django 4.2.4 on 2023-09-11 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_room_reserver_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='reserver_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]