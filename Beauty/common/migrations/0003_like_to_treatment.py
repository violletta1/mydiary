# Generated by Django 4.2.4 on 2023-08-04 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('treatments', '0001_initial'),
        ('common', '0002_comment_to_treatment'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='to_treatment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='treatments.treatment'),
            preserve_default=False,
        ),
    ]