# -*- coding: utf-8 -*-

import json
from datetime import date, timedelta, datetime
import wikipedia
import requests

from users.models import Team


class DatasManager:
    """ Class for the management of the datas """
    def __init__(self):
        pass

    def league_infos_extraction(self):
        """ Extracting game infos from json file """
        url = "https://api-nba-v1.p.rapidapi.com/teams/league/standard"

        headers = {
            'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
            'x-rapidapi-key': "de42e7f1dcmsh2072ecc62d751f3p11e33cjsndbb29dec59a2"
        }

        response = requests.request("GET", url, headers=headers)

        return json.loads(response.text)

    def get_teams_from_json(self, json_loads):
        nba_teams_list = []
        for team in json_loads["api"]["teams"]:
            nba_team = []
            team_id = team["teamId"]
            name = team["fullName"]
            logo = team["logo"]
            conference = team["leagues"]["standard"]["confName"]
            division = team["leagues"]["standard"]["divName"]
            nba_team.append(team_id)
            nba_team.append(name)
            nba_team.append(logo)
            nba_team.append(conference)
            nba_team.append(division)
            if len(logo) > 0 and len(division) > 0:
                nba_teams_list.append(nba_team)
            else:
                pass
        return nba_teams_list

    def team_insertion(self, nba_teams_list):
        for team_list in nba_teams_list:
            team_name = team_list[0]
            team_pic = team_list[1]
            team_conf = team_list[2]
            team_div = team_list[3]
            insertion_datas = Team(name=team_name, picture=team_pic, conference=team_conf, division=team_div)
            insertion_datas.save()

    def get_teams_names(self, nba_teams_list):
        teams_names = []
        for team in nba_teams_list:
            team_couple = []
            team_name = team[1]
            team_id = team[0]
            team_name = team_name.replace(' ', '_')
            team_couple.append(team_id)
            team_couple.append(team_name)
            teams_names.append(team)
        return teams_names


datas = DatasManager()
extract = DatasManager.league_infos_extraction(datas)
json_extract = DatasManager.get_teams_from_json(datas, extract)
print(DatasManager.get_teams_names(datas, json_extract))
