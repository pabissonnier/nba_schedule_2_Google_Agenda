# Generated by Django 3.0.3 on 2020-02-20 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='bio',
            new_name='picture',
        ),
        migrations.AddField(
            model_name='team',
            name='conference',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='team',
            name='division',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='team',
            name='stadium',
            field=models.CharField(default='', max_length=50),
        ),
    ]