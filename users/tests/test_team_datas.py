import users.team_datas as script
from django.test import TestCase
import json
import requests

test_teams_datas = script.TeamInfos()


class TeamDatasTestCase(TestCase):
    team_id = 25
    url = "https://api-nba-v1.p.rapidapi.com/games/teamId/25"

    headers = {
        'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
        'x-rapidapi-key': "de42e7f1dcmsh2072ecc62d751f3p11e33cjsndbb29dec59a2"
    }

    response = requests.request("GET", url, headers=headers)
    json_loads = json.loads(response.text)

    last_games = [['2020-02-29', ':', 'Milwaukee Bucks', '133', ' @ ', 'Oklahoma City Thunder', '86'],
     ['2020-03-04', ':', 'Oklahoma City Thunder', '94', ' @ ', 'LA Clippers', '109'],
     ['2020-03-05', ':', 'Detroit Pistons', '107', ' @ ', 'Oklahoma City Thunder', '114'],
     ['2020-03-07', ':', 'New York Knicks', '103', ' @ ', 'Oklahoma City Thunder', '126'],
     ['2020-03-08', ':', 'Boston Celtics', '104', ' @ ', 'Oklahoma City Thunder', '105']]

    def test_api_connexion(self):
        assert script.TeamInfos.team_api_connexion(test_teams_datas, self.team_id) == self.json_loads

    def test_get_infos_from_json(self):
        assert script.TeamInfos.get_infos_from_json(test_teams_datas, self.json_loads) == self.last_games
