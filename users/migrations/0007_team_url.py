# Generated by Django 2.2 on 2020-02-23 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200223_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='url',
            field=models.CharField(default='', max_length=100),
        ),
    ]
