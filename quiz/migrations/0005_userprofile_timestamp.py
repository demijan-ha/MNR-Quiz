# Generated by Django 3.1 on 2020-08-27 09:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20200827_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
