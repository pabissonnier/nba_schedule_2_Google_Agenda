# -*- coding: utf-8 -*-

import urllib.request
import json
import requests
from datetime import date, timedelta
#from answer.models import Product


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
            vteam = game["vTeam"]["fullName"]
            hteam = game["hTeam"]["fullName"]
            nba_game.append(game_date)
            nba_game.append(vteam)
            nba_game.append(hteam)
            nba_game_list.append(nba_game)
        return nba_game_list

