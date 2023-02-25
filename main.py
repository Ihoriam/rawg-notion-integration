import sys

sys.path.insert(0, 'rawg_integration')
sys.path.insert(0, 'notion_integration')
# print(sys.path)

from rawg_integration.rawg_api import RawgAPI
from notion_integration.notion_api import NotionAPI
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

rawg_api = RawgAPI(api_key=config.get('API_KEYS', 'rawg_api_key'))

notion_api = NotionAPI(
    integration_token=config.get('API_KEYS', 'notion_integration_token'),
    database_id=config.get('API_KEYS', 'notion_database_id')
)

game_title = "Dark Souls"
game = rawg_api.search_game(game_title)
print(game)

game_details = rawg_api.get_game_details_by_id(game.id)
print(game_details)

if game:
    notion_api.add_game(game_details)
else:
    print("No results found for that game title.")
