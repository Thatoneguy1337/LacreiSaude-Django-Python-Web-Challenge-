# Generated by Django 5.0.6 on 2024-07-06 21:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('professionals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professionals.professionals')),
            ],
            options={
                'ordering': ['appointment_date'],
                'unique_together': {('professional', 'appointment_date')},
            },
        ),
    ]
