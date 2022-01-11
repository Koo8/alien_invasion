import pygame

class MyBullet(pygame.sprite.Sprite):
    def __init__(self, game):
        # use sprites for grouping the bullets
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.width = 15
        self.height = 3
        self.bullet_speed = 1.0
        self.color = (10,10, 10)

        self.rect = pygame.Rect(0,0,self.width, self.height)
        self.rect.midleft = game.myship.rect.midright
        self.x = float(self.rect.x)

    def update(self) -> None:
        self.x += self.bullet_speed
        self.rect.x = self.x

    def draw_mybullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
