# -*- coding: utf-8 -*-

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from difflib import SequenceMatcher


class Schedule(models.Model):
    date = models.CharField(max_length=25, null=True)
    hour = models.CharField(max_length=25, null=True)
    vteam = models.CharField(max_length=25, null=True)
    hteam = models.CharField(max_length=25, null=True)
    ingredients = models.CharField(max_length=5000, null=True)
    shops = models.CharField(max_length=1000, null=True)
    link = models.CharField(max_length=1000, null=True, unique=True)
    picture = models.URLField()
    favorites = models.ManyToManyField(User, related_name='favorite', blank=True)
    labels = models.CharField(max_length=1000, null=True)
