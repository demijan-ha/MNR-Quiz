# Generated by Django 3.1 on 2020-08-27 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_userprofile_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]