# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class Schedule(models.Model):
    date = models.CharField(max_length=25, null=True)
    hour = models.CharField(max_length=25, null=True)
    vteam = models.CharField(max_length=25, null=True)
    hteam = models.CharField(max_length=25, null=True)
    game_type = models.CharField(max_length=25, null=True)

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

    def extraction_to_gformat(self, game, teams_chosen):
        global summary
        event = {}
        hteam = game.hteam
        vteam = game.vteam
        gamed = game.date
        gameh = datetime.strptime(game.hour, '%H:%M')
        gameh_end = gameh + timedelta(hours=3)
        if hteam in teams_chosen:
            summary = hteam+' VS '+vteam
        elif vteam in teams_chosen:
            summary = vteam + ' @ '+hteam
        start_date = gamed+'T'+ datetime.strftime(gameh, '%H:%M:%S')
        end_date = gamed+'T'+datetime.strftime(gameh_end, '%H:%M:%S')
        location = "Stadium"
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



