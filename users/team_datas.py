import requests
import json


class TeamInfos:
    def __init__(self):
        pass

    def team_api_connexion(self, team_id):
        url = "https://api-nba-v1.p.rapidapi.com/games/teamId/{0}".format(team_id)

        headers = {
            'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
            'x-rapidapi-key': "de42e7f1dcmsh2072ecc62d751f3p11e33cjsndbb29dec59a2"
        }

        response = requests.request("GET", url, headers=headers)

        json_loads = json.loads(response.text)

        return json_loads

    def get_infos_from_json(self, json_loads):
        """ Get infos from games API """
        nba_game_list = []
        for game in json_loads["api"]["games"]:
            game_list = []
            date = game["startTimeUTC"][:10]
            hteam = game["hTeam"]["fullName"]
            vteam = game["vTeam"]["fullName"]
            hteam_score = game["hTeam"]["score"]["points"]
            vteam_score = game["vTeam"]["score"]["points"]
            game_list.append(date)
            game_list.append(hteam)
            game_list.append(hteam_score)
            game_list.append(vteam)
            game_list.append(vteam_score)
            nba_game_list.append(game_list)
        return nba_game_list