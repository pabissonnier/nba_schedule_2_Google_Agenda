# -*- coding: utf-8 -*-

from .models import Schedule


def get_teams_agenda(team_list):
    schedule_list = []
    for team in team_list:
        team_db_h = Schedule.objects.filter(hteam=team).values("id", "date", "hour", "vteam", "hteam")
        team_db_v = Schedule.objects.filter(vteam=team).values("id", "date", "hour", "vteam", "hteam")
        schedule_list.append(team_db_h)
        schedule_list.append(team_db_v)
    return schedule_list
