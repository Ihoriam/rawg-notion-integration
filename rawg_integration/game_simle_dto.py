class GameSimpleDto:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"GameSimpleDto(id={self.id}, name={self.name})"
