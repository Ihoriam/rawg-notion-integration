import requests

from .game_dto import GameDto
from .game_simple_dto import GameSimpleDto


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
        url = f"https://api.rawg.io/api/games/{id}"
        params = {
            "key": self.api_key
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # Platforms & Genres: extract names as lists of strings
        platforms = data.get("platforms", [])
        platform_names = [p["platform"]["name"] for p in platforms if "platform" in p and "name" in p["platform"]]
        genres = data.get("genres", [])
        genre_names = [g["name"] for g in genres if "name" in g]

        return GameDto(
            id=data.get("id"),
            name=data.get("name"),
            status="Backlog",
            rating=data.get("metacritic", 0),
            release_date=data.get("released", ""),
            genre=genre_names,
            platform=platform_names,
            description=data.get("description_raw") or data.get("description", ""),
            background_image=data.get("background_image", "")
        )
