# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Schedule(models.Model):
    date = models.CharField(max_length=25, null=True)
    hour = models.CharField(max_length=25, null=True)
    vteam = models.CharField(max_length=25, null=True)
    hteam = models.CharField(max_length=25, null=True)
    game_type = models.CharField(max_length=25, null=True)
