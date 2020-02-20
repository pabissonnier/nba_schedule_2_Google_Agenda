# Generated by Django 3.0.3 on 2020-02-20 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_team_stadium'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='player',
            name='name',
        ),
        migrations.AddField(
            model_name='player',
            name='active',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='player',
            name='birthdate',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='player',
            name='college',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='player',
            name='country',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='player',
            name='debut',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='player',
            name='firstname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='player',
            name='height',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='player',
            name='lastname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='player',
            name='number',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='player',
            name='position',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='player',
            name='weight',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='player',
            name='years',
            field=models.CharField(default='', max_length=100),
        ),
    ]
