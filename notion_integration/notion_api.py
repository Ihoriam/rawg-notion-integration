import json

import requests


class NotionAPI:
    def __init__(self, integration_token, database_id):
        self.integration_token = integration_token
        self.database_id = database_id
        self.headers = {
            "Authorization": "Bearer " + self.integration_token,
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28",
        }

    def get_pages(self, num_pages=None):
        readUrl = f"https://api.notion.com/v1/databases/{self.database_id}/query"

        get_all = num_pages is None
        page_size = 100 if get_all else num_pages
        payload = {"page_size": page_size}

        res = requests.request("POST", readUrl, json=payload, headers=self.headers)

        data = res.json()

        print(res.status_code)

        with open('.temp/full-properties.json', 'w', encoding='utf8') as f:
            json.dump(data, f, ensure_ascii=False)

        results = data["results"]
        while data["has_more"] and get_all:
            payload = {"page_size": page_size, "start_cursor": data["next_cursor"]}
            url = f"https://api.notion.com/v1/databases/{self.database_id}/query"
            response = requests.post(url, json=payload, headers=self.headers)
            data = response.json()
            results.extend(data["results"])

        return results

    def create_page(self, data: dict):
        create_url = "https://api.notion.com/v1/pages"

        payload = {
            "parent": {"database_id": self.database_id},
            "cover": {
                "external": {
                    "url": "https://upload.wikimedia.org/wikipedia/commons/6/62/Tuscankale.jpg"
                }
            },
            "properties": data
        }

        res = requests.post(create_url, headers=self.headers, json=payload)
        # print(res.status_code)
        return res

    def add_game(self, title, status, rating, release_date, genre, platform):
        data = {
            "Title": {"title": [{"text": {"content": title}}]},
            "Status": {"select": {"name": status}},
            "Rating": {"number": rating},
            "Release Date": {"date": {"start": release_date}},
            "Genre": {"multi_select": [{"name": genre}] if genre else []},
            "Platform": {"multi_select": [{"name": platform}] if platform else []},
        }
        return self.create_page(data)
