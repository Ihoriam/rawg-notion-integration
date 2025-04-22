import configparser
import tkinter as tk
from tkinter import messagebox

from notion_integration.notion_api import NotionAPI
from plugins.games_rawg.rawg_api import RawgAPI

# Load config
config = configparser.ConfigParser()
config.read('../config.ini')

notion_api = NotionAPI(
    integration_token=config.get('API_KEYS', 'notion_integration_token'),
    database_id=config.get('API_KEYS', 'notion_database_id')
)
rawg_api = RawgAPI(
    api_key=config.get('API_KEYS', 'rawg_api_key')
)


def add_game_to_notion():
    game_title = entry.get()
    if not game_title:
        messagebox.showerror("Input Error", "Please enter a game name.")
        return
    game = rawg_api.search_game(game_title)
    if not game:
        messagebox.showerror("Not Found", f"Game '{game_title}' not found on RAWG.")
        return
    details = rawg_api.get_game_details_by_id(game.id)
    # Prepare data for Notion using all GameDto fields
    res = notion_api.add_game(
        title=details.name,
        status=details.status,
        rating=details.rating,
        release_date=details.release_date,
        genre=details.genre,
        platform=details.platform
    )
    if res.status_code == 200 or res.status_code == 201:
        messagebox.showinfo("Success", f"Game '{details.name}' added to Notion!")
    else:
        messagebox.showerror("Notion Error", f"Failed to add game. Status: {res.status_code}")


root = tk.Tk()
root.title("Add Game to Notion")

label = tk.Label(root, text="Enter Game Name:")
label.pack(padx=10, pady=5)

entry = tk.Entry(root, width=40)
entry.pack(padx=10, pady=5)

add_button = tk.Button(root, text="Add to Notion", command=add_game_to_notion)
add_button.pack(padx=10, pady=10)

root.mainloop()
