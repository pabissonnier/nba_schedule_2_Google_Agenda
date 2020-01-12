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

    def games_extraction(self):
        """ Extracting game infos from json file """
        url = "https://api-nba-v1.p.rapidapi.com/games/date/2020-01-19"

        headers = {
            'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
            'x-rapidapi-key': "de42e7f1dcmsh2072ecc62d751f3p11e33cjsndbb29dec59a2"
        }

        response = requests.request("GET", url, headers=headers)

        nba_text = response.text
