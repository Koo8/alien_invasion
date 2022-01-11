import pygame


class Solider(pygame.sprite.Sprite):
    def __init__(self, game):
        super(Solider, self).__init__()
        self.screen = game.screen

        self.image = pygame.image.load('raindrop_small.bmp')
        self.rect = self.image.get_rect()
        self.DISANCE = 50
        self.SPEED = 0.5
        self.x = float(self.rect.x)

    def update(self) -> None:
        self.x -= self.SPEED
        self.rect.x = self.x


''' Don't need draw method, as we will use group.draw() if rect value and image are provided'''
    # def draw_solider(self):
    #     self.screen.blit(self.image, self.rect)
