# Generated by Django 4.2.4 on 2023-09-18 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_delete_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='room',
        ),
        migrations.AddField(
            model_name='room',
            name='hotel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.hotel'),
            preserve_default=False,
        ),
    ]
