import json

import requests

from game_dto import GameDto
from game_simle_dto import GameSimpleDto


class RawgAPI:
    base_url = "https://api.rawg.io/api/"

    def __init__(self, api_key):
        self.api_key = api_key

    def search_game(self, game_title):
        search_url = self.base_url + "games"
        params = {
            "search": game_title,
            "key": self.api_key
        }
        response = requests.get(search_url, params=params)
        response_json = response.json()

        if response_json["results"]:
            game = response_json["results"][0]
            return GameSimpleDto(
                id=game["id"],
                name=game["name"]
            )
        else:
            return None

    def get_game_details_by_id(self, id):
        details_url = self.base_url + "games/" + str(id)
        params = {
            "key": self.api_key
        }
        response = requests.get(details_url, params=params)
        response_json = response.json()

        with open('.temp/game-details.json', 'w', encoding='utf8') as f:
            json.dump(response_json, f, ensure_ascii=False)


        return GameDto(
            id=response_json["id"],
            name=response_json["name"],
            description=response_json["description"],
            background_image=response_json["background_image"],
            released=response_json["released"],
            platforms=response_json["platforms"],
            metacritic=response_json["metacritic"]
        )
