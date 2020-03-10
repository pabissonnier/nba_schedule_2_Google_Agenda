# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class Schedule(models.Model):
    date = models.CharField(max_length=25, null=True)
    hour = models.CharField(max_length=25, null=True)
    vteam = models.CharField(max_length=25, null=True)
    hteam = models.CharField(max_length=25, null=True)
    arena = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.date

    def get_teams_agenda(self, team_list):
        games_list = []
        for team in team_list:
            team_db_h = Schedule.objects.filter(hteam=team)
            team_db_v = Schedule.objects.filter(vteam=team)
            games_list.append(team_db_h)
            games_list.append(team_db_v)
        return games_list

    def extraction_to_gformat(self, game):
        global summary
        event = {}
        hteam = game.hteam
        vteam = game.vteam
        gameh = game.hour #string
        game_day = game.date
        gameh_dt = datetime.strptime(gameh, '%H:%M')
        gameh_end = datetime.strftime(gameh_dt + timedelta(hours=1), '%H:%M')
        gameh_end_dt = datetime.strptime(gameh_end, '%H:%M')
        if gameh_end_dt < gameh_dt:
            gamed = datetime.strptime(game_day, '%Y-%m-%d') + timedelta(days=1)
        else:
            gamed = datetime.strptime(game_day, '%Y-%m-%d')

        summary = vteam + ' @ '+hteam
        start_date = datetime.strftime(gamed, '%Y-%m-%d') + 'T' + datetime.strftime(gameh_dt, '%H:%M') + ':00'
        end_date = datetime.strftime(gamed, '%Y-%m-%d') + 'T' + datetime.strftime(gameh_end_dt, '%H:%M') + ':00'
        location = game.arena
        description = "Your schedule from NS2GC"
        timezone = "America/New_York"
        event['summary'] = summary
        event['location'] = location
        event['description'] = description
        event['start'] = {}
        event['start']['dateTime'] = start_date
        event['start']['timeZone'] = timezone
        event['end'] = {}
        event['end']['dateTime'] = end_date
        event['end']['timeZone'] = timezone
        return event

