# Generated by Django 2.1 on 2021-03-28 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0003_register'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='email',
        ),
        migrations.RemoveField(
            model_name='register',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='register',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='register',
            name='uname',
        ),
    ]