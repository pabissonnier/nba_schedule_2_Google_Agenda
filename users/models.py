from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=100)
    picture = models.CharField(max_length=250)
    conference = models.CharField(max_length=100, default='')
    division = models.CharField(max_length=100, default='')
    favorite = models.ManyToManyField(User, related_name='favorite', blank=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    firstname = models.CharField(max_length=100, default='')
    lastname = models.CharField(max_length=100, default='')
    team = models.CharField(max_length=100, default='', primary_key=True)
    years = models.CharField(max_length=100, default='')
    college = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=100, default='')
    birthdate = models.CharField(max_length=100, default='')
    debut = models.CharField(max_length=100, default='')
    height = models.CharField(max_length=100, default='')
    weight = models.CharField(max_length=100, default='')
    number = models.CharField(max_length=100, default='')
    active = models.CharField(max_length=100, default='')
    position = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.lastname
