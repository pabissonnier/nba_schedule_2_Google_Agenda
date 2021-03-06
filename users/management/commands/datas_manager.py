# -*- coding: utf-8 -*-

import json
from datetime import date, timedelta, datetime
import wikipedia
import requests

from users.models import Team
from users.models import Player


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
        json_loads = json.loads(response.text)
        return json_loads

    def get_teams_from_json(self, json_loads):
        """ Get team infos from the api extraction """
        nba_teams_list = []
        for team in json_loads["api"]["teams"]:
            nba_team = []
            id = team["teamId"]
            name = team["fullName"]
            logo = team["logo"]
            conference = team["leagues"]["standard"]["confName"]
            division = team["leagues"]["standard"]["divName"]
            nba_team.append(id)
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
        """ Insertion of the datas into the database """
        for team_list in nba_teams_list:
            team_id = team_list[0]
            team_name = team_list[1]
            team_pic = team_list[2]
            team_conf = team_list[3]
            team_div = team_list[4]
            insertion_datas = Team(team_id=team_id, name=team_name, picture=team_pic, conference=team_conf, division=team_div)
            data_already = Team.objects.filter(team_id=team_id)
            if not data_already:
                insertion_datas.save()

    def get_teams_names(self, nba_teams_list):
        """ Get the names of the teams to display more infos """
        teams_names = []
        for team in nba_teams_list:
            team_couple = []
            team_name = team[1]
            team_id = team[0]
            team_couple.append(team_id)
            team_couple.append(team_name)
            teams_names.append(team_couple)
        return teams_names

    def get_nba_players(self, teams_names):
        """ for each team name, we get the players infos to display them in
        players detail template """
        for team in teams_names:
            team_id = team[0]
            team_name = team[1]
            url = "https://api-nba-v1.p.rapidapi.com/players/teamId/{0}".format(team_id)
            headers = {
            'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
            'x-rapidapi-key': "de42e7f1dcmsh2072ecc62d751f3p11e33cjsndbb29dec59a2"
            }

            json_loads = json.loads(requests.request("GET", url, headers=headers).text)

            for player in json_loads["api"]["players"]:
                f_name = player["firstName"]
                l_name = player["lastName"]
                years = player["yearsPro"]
                college = player["collegeName"]
                country = player["country"]
                b_date = player["dateOfBirth"]
                height = player["heightInMeters"]
                weight = player["weightInKilograms"]
                if "standard" in player['leagues']:
                    number = player["leagues"]["standard"]["jersey"]
                    active = player["leagues"]["standard"]["active"]
                    position = player["leagues"]["standard"]["pos"]
                    insertion_datas = Player(firstname=f_name, lastname=l_name, team=team_name,
                                             years=years,
                                             college=college, country=country, birthdate=b_date,
                                             height=height,
                                             weight=weight, number=number, active=active,
                                             position=position, )
                    insertion_datas.save()
