# Generated by Django 2.1 on 2021-07-03 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0009_auto_20210702_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptoms', models.CharField(max_length=250)),
                ('complains', models.CharField(max_length=250)),
                ('bp', models.CharField(max_length=250)),
                ('temperature', models.CharField(max_length=250)),
                ('weight', models.CharField(max_length=250)),
                ('fever', models.CharField(max_length=250)),
                ('pain_condition', models.CharField(max_length=250)),
                ('physical_appearence', models.CharField(max_length=250)),
                ('Deformation', models.CharField(max_length=250)),
                ('appetite', models.CharField(max_length=250)),
                ('sleep_conditions', models.CharField(max_length=250)),
            ],
        ),
    ]