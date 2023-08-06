# Generated by Django 4.2.4 on 2023-08-06 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('treatments', '0003_treatment_photo_treatment'),
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='treatment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='treatments.treatment'),
        ),
    ]
