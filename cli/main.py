import configparser
import sys
from datetime import datetime, timezone

sys.path.insert(0, './plugins/games_rawg')
sys.path.insert(0, './notion_integration')

from plugins.games_rawg.rawg_api import RawgAPI
from notion_integration.notion_api import NotionAPI


def notion_api_add_test():
    pages = notion_api.get_pages()
    for page in pages:
        page_id = page["id"]
        props = page["properties"]
        name = props["Title"]["title"][0]["text"]["content"]
        print(name)
    title = "Elder ring 2"
    release_date = datetime.strptime('09-19-2020', '%m-%d-%Y').astimezone(timezone.utc).isoformat()
    description = "Test Description"
    data = {
        "Title": {"title": [{"text": {"content": title}}]},
    }
    notion_api.create_page(data)


def rawg_api_search_test():
    game_title = "Dark Souls"
    game = rawg_api.search_game(game_title)
    print(game)
    game_details = rawg_api.get_game_details_by_id(game.id)
    print(game_details)


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('../config.ini')

    notion_api = NotionAPI(
        integration_token=config.get('API_KEYS', 'notion_integration_token'),
        database_id=config.get('API_KEYS', 'notion_database_id')
    )

    rawg_api = RawgAPI(
        api_key=config.get('API_KEYS', 'rawg_api_key')
    )

    # notion_api_add_test()
    rawg_api_search_test()
