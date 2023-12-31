# Generated by Django 4.2.4 on 2023-09-11 07:42

from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField(default=0)),
                ('date_reserved', models.DateField(auto_now_add=True)),
                ('resrved', models.BooleanField(default=False)),
                ('date_unreserved', models.DateField(default=users.models.get_date_time)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.hotel')),
            ],
        ),
    ]
