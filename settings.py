'''Use Settings class to store all setting-related constant values. so that it is easier
to modify the game as it grows of its appearance and behavior'''
import pygame

class Settings:
    ''' A class to store all settings for the game '''
    def __init__(self):
       '''initialize the game's settings.'''
       #Screen settings
       self.screen_width = 1200
       self.screen_height = 800
       self.bg_color = (255, 255, 255)
       # ship settings
       self.ship_limit = 3
       # bullets settings
       self.bullet_width = 3
       self.bullet_height = 15
       self.bullet_color = (60,60,60)
       self.bullet_allowed = 3

       # display setting
       self.font = pygame.font.SysFont(None, 48)
       self.text_color = (0, 0, 255)
       self.button_color = (0, 255, 0)
       self.score_scale = 50

       # aliens setting
       self.alien_drop_speed = 20.0
       self.speed_up_scale =.2
       self.reset_speed()



    def speed_up_game(self):
       print(f'IN speed up game ()')
       self.bullet_speed *= self.speed_up_scale
       self.alien_speed *= self.speed_up_scale
       self.ship_speed *= self.speed_up_scale

    def reset_speed(self):
       self.bullet_speed = 1.0
       self.alien_speed = 0.5
       self.ship_speed = 2.0

    def reset_higher_speed(self):
       self.speed_up_game()







