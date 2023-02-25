from typing import List, Dict


class GameDto:
    def __init__(self,
                 id: int,
                 name: str,
                 description: str,
                 background_image: str,
                 released: str,
                 platforms: List[Dict],
                 metacritic: int):
        self.id = id
        self.name = name
        self.description = description
        self.background_image = background_image
        self.released = released
        self.platforms = platforms
        self.metacritic = metacritic

    def __str__(self):
        return f"GameDto(\nid={self.id},\nname={self.name},\ndescription={self.description[:20]}...,\n" \
               f"background_image={self.background_image},\nreleased={self.released},\n" \
               f"platforms={self.platforms},\nmetacritic={self.metacritic}\n)"
