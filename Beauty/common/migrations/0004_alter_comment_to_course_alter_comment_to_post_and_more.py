# Generated by Django 4.2.4 on 2023-08-05 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('diary', '0001_initial'),
        ('treatments', '0002_treatment_user'),
        ('common', '0003_like_to_treatment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='to_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='to_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='diary.post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='to_treatment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='treatments.treatment'),
        ),
        migrations.AlterField(
            model_name='like',
            name='to_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
        migrations.AlterField(
            model_name='like',
            name='to_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='diary.post'),
        ),
        migrations.AlterField(
            model_name='like',
            name='to_treatment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='treatments.treatment'),
        ),
    ]