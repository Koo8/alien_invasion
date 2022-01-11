import pygame

class Game_Stats:
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings

        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.ship_left = self.settings.ship_limit
        # score needs to be reset each game
        self.score = 0

