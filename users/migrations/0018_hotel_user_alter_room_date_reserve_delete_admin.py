# Generated by Django 4.2.4 on 2023-09-18 09:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0017_alter_room_reserver_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='date_reserve',
            field=models.DateField(default=datetime.date(2023, 9, 18), null=True),
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
    ]
