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
            team_couple.append(team_id)
            team_couple.append(team_name)
            teams_names.append(team_couple)
        return teams_names

    def get_nba_players(self, teams_names):
        nba_players_list = []
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
                nba_player = []
                f_name = player["firstName"]
                l_name = player["lastName"]
                years = player["yearsPro"]
                college = player["collegeName"]
                country = player["country"]
                b_date = player["dateOfBirth"]
                debut = player["startNba"]
                height = player["heightInMeters"]
                weight = player["weightInKilograms"]
                if "standard" in player['leagues']:
                    number = player["leagues"]["standard"]["jersey"]
                    active = player["leagues"]["standard"]["active"]
                    position = player["leagues"]["standard"]["pos"]
                    nba_player.append(f_name)
                    nba_player.append(l_name)
                    nba_player.append(team_name)
                    nba_player.append(years)
                    nba_player.append(college)
                    nba_player.append(country)
                    nba_player.append(b_date)
                    nba_player.append(debut)
                    nba_player.append(height)
                    nba_player.append(weight)
                    nba_player.append(number)
                    nba_player.append(active)
                    nba_player.append(position)
                    nba_players_list.append(nba_player)
                return nba_players_list

    def players_insertion(self, nba_players_list):
        """ Insert players in the DB """
        for player_list in nba_players_list:
            game_date = game_list[0]
            game_hour = game_list[1]
            game_vteam = game_list[2]
            game_hteam = game_list[3]
            game_type = "season"
            insertion_datas = Schedule(date=game_date, hour=game_hour, vteam=game_vteam, hteam=game_hteam,
                                       game_type=game_type)
            insertion_datas.save()
