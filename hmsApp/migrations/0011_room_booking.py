# Generated by Django 5.0.1 on 2024-01-30 06:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsApp', '0010_remove_room_hotel_delete_booking_delete_room'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.IntegerField(primary_key=True, serialize=False)),
                ('room_name', models.CharField(default=True, max_length=50)),
                ('room_category', models.CharField(choices=[('QUEEN', 'QUEEN'), ('NON-AC', 'NON-AC'), ('AC', 'AC'), ('DELUX', 'DELUX'), ('KING', 'KING')], max_length=10)),
                ('beds', models.IntegerField()),
                ('max_capacity', models.IntegerField()),
                ('room_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('roomImage', models.ImageField(upload_to='room_pics')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hmsApp.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('num_guests', models.PositiveIntegerField()),
                ('num_rooms', models.PositiveIntegerField()),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='hmsApp.room')),
            ],
        ),
    ]
