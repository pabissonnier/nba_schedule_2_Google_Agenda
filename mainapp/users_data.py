# -*- coding: utf-8 -*-


def get_teams(request):
    teams_list = request.POST.getlist('team')
    return teams_list
