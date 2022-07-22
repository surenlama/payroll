# Generated by Django 2.1 on 2021-03-28 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=250)),
                ('car_img', models.FileField(upload_to='media')),
                ('car_desc', models.TextField(max_length=250)),
                ('added_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]