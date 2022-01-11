'''Use Ship class to manage behavior of player's ship '''

import pygame

class Ship:
    def __init__(self, ai_game): # game instance so that the ship rectangle can have access to game resources
        ''' Initialize the ship, set its starting position '''

        # access game screen and its rect, and settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # load ship image and get its rect
        self.image = pygame.image.load('image/ship_small.bmp')
        self.rect = self.image.get_rect()

        # start new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # a flag for moving the ship
        self.moving_right = False
        self.moving_left = False

        # fine tune ship speed needs to be float
        self.x = float(self.rect.x)

    def blitme(self):
        ''' Draw ship at its current location '''
        self.screen.blit(self.image, self.rect)

    def update(self):
        # first fine tune self.x into float
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # then assign self.x to self.rect.x
        self.rect.x = self.x

    def recenter(self):
        self.rect.midbottom = self.screen_rect.midbottom
        # this line is important, self.x determine the location of ship from update() algorithm
        self.x = self.rect.x
