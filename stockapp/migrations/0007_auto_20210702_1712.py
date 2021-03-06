# Generated by Django 2.1 on 2021-07-02 17:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stockapp', '0006_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Addproduct',
            new_name='Addpatient',
        ),
        migrations.RenameField(
            model_name='addpatient',
            old_name='product_desc',
            new_name='patient_desc',
        ),
        migrations.RenameField(
            model_name='addpatient',
            old_name='product_img',
            new_name='patient_img',
        ),
        migrations.RenameField(
            model_name='addpatient',
            old_name='product_name',
            new_name='patient_name',
        ),
        migrations.RenameField(
            model_name='addpatient',
            old_name='product_price',
            new_name='patient_price',
        ),
    ]
