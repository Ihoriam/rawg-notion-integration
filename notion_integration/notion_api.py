from notion_client import Client


class NotionAPI:
    def __init__(self, integration_token, database_id):
        self.client = Client(auth=integration_token)
        self.database_id = database_id

    def add_game(self, game):
        new_game = {
            "Title": {"title": [{"text": {"content": game.name}}]},
            "Notes": {"rich_text": [{"text": {"content": game.description}}]}
        }

        self.client.pages.create(parent={"database_id": self.database_id}, properties=new_game)
