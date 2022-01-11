'''A row of raindrop go down the screen, disappear,
then a new row of rain drop resurface at the top of the screen'''
import sys

import pygame

class RainDrop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('raindrop_small.bmp')
        self.rect = self.image.get_rect()
        self.rect.topleft = (10, 10)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.raindrops = pygame.sprite.Group()



    def _fill_with_raindrops(self):
        # how many drops can be drawn
        num = (self.screen_rect.width - 20) // (self.rect.width *2)
        for n in range(num):
            rain = RainDrop()
            rain.x = n * rain.rect.width *2 + 40
            rain.rect.x = rain.x
            self.raindrops.add(rain)


    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(pygame.Color(0,255,0))
        self.raindrops.draw(self.screen)
        pygame.display.flip()

    def _raining(self):
        self._check_if_group_empty()
        self._keep_on_raining()

    def _check_if_group_empty(self):
        if not self.raindrops:
            self._fill_with_raindrops()

    def _keep_on_raining(self):
        for rain in self.raindrops.sprites():
            if rain.rect.top >= rain.screen_rect.bottom:
                self.raindrops.remove(rain)
            else:
                rain.y +=1.0
                rain.rect.y = rain.y



    def run(self):
        while True:
            self._check_event()
            self._raining() # update new location
            self._update_screen()





if __name__ == "__main__":
    game = RainDrop()
    game.run()