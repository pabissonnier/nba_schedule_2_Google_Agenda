from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=100)
    picture = models.CharField(max_length=250)
    conference = models.CharField(max_length=25, default='')
    division = models.CharField(max_length=25, default='')
    stadium = models.CharField(max_length=50, default='')
    favorite = models.ManyToManyField(User, related_name='favorite', blank=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=250)
    team = models.OneToOneField(
        Team,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.name
