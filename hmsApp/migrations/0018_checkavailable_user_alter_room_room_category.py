# Generated by Django 5.0.1 on 2024-01-31 21:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsApp', '0017_room_available_room_room_available_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='checkavailable',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_category',
            field=models.CharField(choices=[('Single Room', 'Single Room'), ('Double Room', 'Double Room'), ('King Room', 'King Room'), ('Double-Double Room', 'Double-Double Room'), ('Twin Room', 'Twin Room'), ('Queen Room', 'Queen Room')], max_length=20),
        ),
    ]