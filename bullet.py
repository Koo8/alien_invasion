import pygame
# use Sprites because there are a lot of bullets going into a group

class Bullet(pygame.sprite.Sprite):
    def __init__(self, ai_game):
        # inherent parent Sprite class
        super().__init__()
        # for accessing ai_game instance attributes
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # draw a bullet rect and set its position
        self.rect = pygame.Rect(0,0,self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # use float for bullet y value for fine tune movement
        self.y = float(self.rect.y)

    def update(self): # overide the built_in update method
        ''' change y position for upshooting effect '''
        self.y -= self.settings.bullet_speed # this is a float
        #update rect y  value
        self.rect.y = self.y # rect only take the integer part

    def draw_bullet(self):  # not blit, no preset image
        pygame.draw.rect(self.screen, self.color,self.rect)

