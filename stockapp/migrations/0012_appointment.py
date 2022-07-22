# Generated by Django 2.1 on 2021-07-03 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0011_screening_patient_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.CharField(max_length=250)),
                ('full_name', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=250)),
                ('message', models.CharField(max_length=250)),
            ],
        ),
    ]
