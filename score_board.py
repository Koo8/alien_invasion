"""
display the score
make scoreboard
update scoreboard as aliens shot down
reset scoreboard
in case bullets are wide, score all hits
increase point value
round the score
save and display the highscore
display level
display number of ships
"""

import pygame

class  Scoreboard:
    '''A class to report scores, levels, high score and number of ships left'''
    def __init__(self, ai_game):
        # pass all needed values from the game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.text_color = self.settings.text_color
        self.font = self.settings.font

        self.prep_scoreboard()

    def prep_scoreboard(self):
        # display score, highscore, level and number of ships
        self.update_score()

    def update_score(self):
        self.score_str = str(self.stats.score)
        self.score_img = self.font.render(self.score_str, True,self.text_color, self.settings.bg_color)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_scoreboard(self):
        self.screen.blit(self.score_img, self.score_rect)





