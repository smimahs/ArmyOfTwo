# Generated by Django 3.0.8 on 2020-11-04 07:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0004_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='auther',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
    ]