# Generated by Django 2.2 on 2020-03-09 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='game_type',
            new_name='arena',
        ),
    ]
