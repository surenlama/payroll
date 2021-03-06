# Generated by Django 3.2 on 2022-01-02 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0016_remove_addpatient_patient_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='screening',
            old_name='Deformation',
            new_name='attendence',
        ),
        migrations.RenameField(
            model_name='screening',
            old_name='appetite',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='screening',
            old_name='bp',
            new_name='join',
        ),
        migrations.RenameField(
            model_name='screening',
            old_name='patient_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='screening',
            old_name='complains',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='screening',
            old_name='fever',
            new_name='salary',
        ),
        migrations.RenameField(
            model_name='screening',
            old_name='pain_condition',
            new_name='tax',
        ),
        migrations.RenameField(
            model_name='screening',
            old_name='physical_appearence',
            new_name='work',
        ),
        migrations.RemoveField(
            model_name='screening',
            name='sleep_conditions',
        ),
        migrations.RemoveField(
            model_name='screening',
            name='symptoms',
        ),
        migrations.RemoveField(
            model_name='screening',
            name='temperature',
        ),
        migrations.RemoveField(
            model_name='screening',
            name='weight',
        ),
    ]
