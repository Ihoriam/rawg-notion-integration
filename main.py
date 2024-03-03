import sys
from datetime import datetime, timezone

sys.path.insert(0, 'rawg_integration')
sys.path.insert(0, 'notion_integration')
# print(sys.path)

from rawg_integration.rawg_api import RawgAPI
from notion_integration.notion_api import NotionAPI
import configparser


def test_notion_api():
    pages = notion_api.get_pages()
    for page in pages:
        page_id = page["id"]
        props = page["properties"]

        name = props["Title"]["title"][0]["text"]["content"]
        print(name)
        # description = props["Description"]["rich_text"][0]["text"]["content"]
        # print(description)
        # genre = props["Ganre"]["rich_text"][0]["text"]["content"]
        # print(genre)
    title = "Elder ring 2"
    release_date = datetime.strptime('09-19-2020', '%m-%d-%Y').astimezone(timezone.utc).isoformat()
    description = "Test Description"
    data = {
        "Title": {"title": [{"text": {"content": title}}]},
    }
    notion_api.create_page(data)


def test_rawg_api():
    game_title = "Dark Souls"
    game = rawg_api.search_game(game_title)
    print(game)
    game_details = rawg_api.get_game_details_by_id(game.id)
    print(game_details)
    # if game:
    #     notion_api.add_game(game_details)
    # else:
    #     print("No results found for that game title.")


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')

    notion_api = NotionAPI(
        integration_token=config.get('API_KEYS', 'notion_integration_token'),
        database_id=config.get('API_KEYS', 'notion_database_id')
    )

    rawg_api = RawgAPI(
        api_key=config.get('API_KEYS', 'rawg_api_key')
    )

    # test_notion_api()
    test_rawg_api()
