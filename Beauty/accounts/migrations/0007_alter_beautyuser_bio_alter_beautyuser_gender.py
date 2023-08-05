# Generated by Django 4.2.4 on 2023-08-05 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_beautyuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beautyuser',
            name='bio',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='beautyuser',
            name='gender',
            field=models.IntegerField(choices=[(1, 'MALE'), (2, 'FEMALE'), (3, 'DO_NOT_SHOW')], default=3),
        ),
    ]