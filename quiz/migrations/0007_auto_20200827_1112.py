# Generated by Django 3.1 on 2020-08-27 09:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20200827_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='End'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Start'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
