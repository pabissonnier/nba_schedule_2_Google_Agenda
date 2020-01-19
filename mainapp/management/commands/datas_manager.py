# -*- coding: utf-8 -*-

import urllib.request
import json
import requests
from datetime import date, timedelta, datetime
from mainapp.models import Schedule


class DatasManager:
    """ Class for the management of the datas """
    def __init__(self):
        pass

    def season_dates(self):
        """ From season, gets every game date """
        date_list = []
        sdate = date(2019, 10, 1)  # start date
        edate = date(2020, 4, 15)  # end date

        delta = edate - sdate  # as timedelta

        for i in range(delta.days + 1):
            day = sdate + timedelta(days=i)
            day_str = day.strftime("%Y-%m-%d")
            date_list.append(day_str)
        return date_list

    def games_extraction(self, date):
        """ Extracting game infos from json file """
        url = "https://api-nba-v1.p.rapidapi.com/games/date/{0}".format(date)

        headers = {
            'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
            'x-rapidapi-key': "de42e7f1dcmsh2072ecc62d751f3p11e33cjsndbb29dec59a2"
        }

        response = requests.request("GET", url, headers=headers)

        return json.loads(response.text)

    def get_infos_from_json(self, day_schedule):
        """ Get infos from schedule API """
        nba_game_list = []
        for game in day_schedule["api"]["games"]:
            nba_game = []
            game_date = game["startTimeUTC"]
            game_day = game_date[:10]
            game_hour = game_date[11:16]
            vteam = game["vTeam"]["fullName"]
            hteam = game["hTeam"]["fullName"]
            nba_game.append(game_day)
            nba_game.append(game_hour)
            nba_game.append(vteam)
            nba_game.append(hteam)
            nba_game_list.append(nba_game)
        return nba_game_list

    def date_converter(self, nba_list):
        """ Convert list timezone to actual NY timezone """
        nba_real_list = []
        for game in nba_list:
            nba_game = []
            nba_hour = datetime.strptime(game[1], '%H:%M')
            nba_hour_time = nba_hour.time()
            nba_real_hour = nba_hour - timedelta(hours=5)
            nba_real_hour_time = nba_real_hour.time()
            nba_day = datetime.strptime(game[0], '%Y-%m-%d')
            if nba_hour_time < nba_real_hour_time:
                nba_real_day = nba_day - timedelta(days=1)
                nba_real_day_date = nba_real_day.date()
            else:
                nba_real_day_date = nba_day.date()
            vteam = game[2]
            hteam = game[3]
            nba_game.append(nba_real_day_date.strftime("%Y-%m-%d"))
            nba_game.append(nba_real_hour_time.strftime("%H:%M"))
            nba_game.append(vteam)
            nba_game.append(hteam)
            nba_real_list.append(nba_game)
        return nba_real_list

    def game_day_insertion(self, nba_real_list):
        """ Insert games of a day in the DB """
        for game_list in nba_real_list:
            game_date = game_list[0]
            game_hour = game_list[1]
            game_vteam = game_list[2]
            game_hteam = game_list[3]
            game_type = "season"
            insertion_datas = Schedule(date=game_date, hour=game_hour, vteam=game_vteam, hteam=game_hteam,
                                       game_type=game_type)
            insertion_datas.save()
