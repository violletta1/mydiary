# Generated by Django 4.2.4 on 2023-08-08 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_beautyuser_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beautyuser',
            name='group',
        ),
    ]
