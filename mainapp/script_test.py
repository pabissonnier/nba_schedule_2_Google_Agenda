import wikipedia
from django.shortcuts import render
from django.http import HttpResponse
from .models import Schedule
from .calendar_insertion import calendar_connection, calendar_insertion, event_insertion

"""wikipedia.set_lang("en")
page = wikipedia.page("National_Basketball_Association#Teams").content
print(page)"""

schedule = Schedule()
teams_list = ["Atlanta Hawks"]

schedule_list = Schedule.get_teams_agenda(schedule, teams_list)
games_list = []
service = calendar_connection()
calendar_id = calendar_insertion(service)
for schedule in schedule_list:
    for game in schedule:
        game_dict = Schedule.extraction_to_gformat(schedule, game, teams_list)
        games_list.append(game_dict)
        for game in games_list:
            print(game)
