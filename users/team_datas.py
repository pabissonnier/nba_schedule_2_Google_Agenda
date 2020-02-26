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

