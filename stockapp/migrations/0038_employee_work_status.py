# Generated by Django 4.0.6 on 2022-07-29 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0037_alter_employee_bonus_alter_employee_join_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='work_status',
            field=models.CharField(choices=[('Parttime', 'Partime'), ('NOrmalTime', 'Normaltime'), ('OverTime', 'Overtime')], default='Parttime', max_length=250),
            preserve_default=False,
        ),
    ]
