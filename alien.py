import pygame

class Alien(pygame.sprite.Sprite):
    ''' a class represent a single alien in a fleet '''
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load('image/alien_small.bmp')#.convert_alpha()  # convert_alpha() speed up the game
        self.rect = self.image.get_rect()

        # start each alien near the top of the screen ->58 and 56 are alien width and height
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store alien horizontal position as a float
        self.x = float(self.rect.x)
        self.speed = self.settings.alien_speed
        self.drop_speed = self.settings.alien_drop_speed

        ''' For this class, we don't draw individual alien to the screen, but use sprites.group method to auto draw all the aliens onto the screen'''

    def update(self) -> None:
        self.x += self.speed
        self.rect.x = self.x

    def check_edge(self): # one alien touch edge will trigger whole fleet to drop and change direction
        if self.rect.right >= self.screen_rect.right or self.rect.left < 0:
            return True