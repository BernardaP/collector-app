# Generated by Django 3.1.7 on 2021-03-10 23:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210310_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeding',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]