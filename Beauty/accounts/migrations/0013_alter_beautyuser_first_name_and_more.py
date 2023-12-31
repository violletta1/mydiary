# Generated by Django 4.2.4 on 2023-08-12 11:22

import Beauty.accounts.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_remove_beautyuser_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beautyuser',
            name='first_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), Beauty.accounts.validators.letters]),
        ),
        migrations.AlterField(
            model_name='beautyuser',
            name='last_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), Beauty.accounts.validators.letters]),
        ),
    ]
