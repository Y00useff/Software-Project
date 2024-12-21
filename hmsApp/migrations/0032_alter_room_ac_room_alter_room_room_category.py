# Generated by Django 5.0.1 on 2024-02-10 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsApp', '0031_alter_room_ac_room_alter_room_room_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='ac_room',
            field=models.CharField(choices=[('Non-AC', 'Non-AC'), ('AC', 'AC')], default=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_category',
            field=models.CharField(choices=[('Double Room', 'Double Room'), ('King Room', 'King Room'), ('Twin Room', 'Twin Room'), ('Queen Room', 'Queen Room'), ('Single Room', 'Single Room'), ('Double-Double Room', 'Double-Double Room')], max_length=20),
        ),
    ]
