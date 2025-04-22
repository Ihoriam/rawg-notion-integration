from typing import List, Optional


class GameDto:
    def __init__(self,
                 id: int,
                 name: str,
                 status: str = "Backlog",
                 rating: Optional[int] = None,
                 release_date: Optional[str] = None,
                 genre: Optional[List[str]] = None,
                 platform: Optional[List[str]] = None,
                 description: str = "",
                 background_image: str = ""):
        self.id = id
        self.name = name
        self.status = status
        self.rating = rating
        self.release_date = release_date
        self.genre = genre or []
        self.platform = platform or []
        self.description = description
        self.background_image = background_image

    def __str__(self):
        return (
            f"GameDto(\n"
            f"  id={self.id},\n"
            f"  name={self.name},\n"
            f"  status={self.status},\n"
            f"  rating={self.rating},\n"
            f"  release_date={self.release_date},\n"
            f"  genre={self.genre},\n"
            f"  platform={self.platform},\n"
            f"  description={self.description[:20]}...,\n"
            f"  background_image={self.background_image}\n"
            f")"
        )
