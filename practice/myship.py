import pygame

class MyShip:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('ship_small.bmp')
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
        self.move_up = False
        self.move_down = False
        self.move_one_step = 1.5

    def update_myship(self):
        if self.move_up:
            if self.rect.top > 0:
                self.y -= self.move_one_step
        elif self.move_down:
            if self.rect.bottom < self.screen_rect.bottom:
                self.y += self.move_one_step
        self.rect.y = self.y
        


    def blitmyship(self):
        self.screen.blit(self.image, self.rect)


