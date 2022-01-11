import sys

import pygame
import random


class Star:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))

        self.x = 10
        self.y = 10
        self.radius  = 20
        self._create_stars()

    def run(self):
        while True:
            self._check_event()
            self._update_screen()
    def _create_stars(self):
        for num in range(10):
            self.x = random.randint(10, self.screen.get_width())
            self.y = random.randint(10, self.screen.get_height())
            self._draw_star()

    def _draw_star(self):
        self.image = pygame.draw.circle(self.screen, (0,0,0),(self.x, self.y),self.radius)

    def _update_screen(self):
        self.screen.fill((200,200,200))
        self._create_stars()
        pygame.display.flip()

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    star = Star()
    star.run()