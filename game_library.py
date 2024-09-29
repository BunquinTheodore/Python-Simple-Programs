from game import *

class GameLibrary:
    def __init__(self):
        self.games = {
            "Donkey Kong": Game("Donkey Kong", 3, 2),
            "Super Mario Bros": Game("Super Mario Bros", 5, 3),
            "Tetris": Game("Tetris", 2, 1)
        }

    def display_available_games(self):
        print("Available Games:")
        for game in self.games.values():
            print(f"{game.name}: Quantity - {game.quantity}, Cost - {game.cost}")
