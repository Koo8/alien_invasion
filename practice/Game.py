import sys

import pygame
from myship import MyShip
from mybullets import MyBullet
from circle_solider import Solider

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Horizontal Game")
        self.screen_height = self.screen.get_height()

        self.myship = MyShip(self)
        self.mybullets = pygame.sprite.Group()
        self.soliders = pygame.sprite.Group()
        self._fill_soliders_to_group_with_specific_rect_value()

    def _fill_soliders_to_group_with_specific_rect_value(self):
        so = Solider(self)
        num_of_soliders = (self.screen.get_height() - so.DISANCE) // (so.rect.height +10)
        for n in range(num_of_soliders):
            solider = Solider(self)
            # specify solider's rect value
            solider.y= (n+1)*so.rect.height +10
            solider.x = (self.screen.get_width() -100)
            solider.rect.x = solider.x
            solider.rect.y = solider.y
            self.soliders.add(solider)

    def _check_all_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_KEYDOWN_events(event)
            elif event.type == pygame.KEYUP:
                self._check_KEYUP_events(event)

    def _check_KEYDOWN_events(self,event):
        if event.key == pygame.K_UP:
            self.myship.move_up = True
        elif event.key == pygame.K_DOWN:
            # print("K_DOWN is pressed")
            self.myship.move_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_my_bullet()

    def _check_KEYUP_events(self, event):
        if event.key == pygame.K_UP:
            self.myship.move_up = False
        elif event.key == pygame.K_DOWN:
            # print("K_DOwn is released")
            self.myship.move_down = False

    def _update_all_elements(self):
        self.myship.update_myship()
        self.mybullets.update()
        self._check_solide_empty()
        self.soliders.update()
        # for bullets vs. soliders collision
        pygame.sprite.groupcollide(self.soliders,self.mybullets, True, True)

    def _draw_screen(self):
        # background
        self.screen.fill((100, 200, 50))
        self.myship.blitmyship()
        for b in self.mybullets.sprites():
            b.draw_mybullet()

        self.soliders.draw(self.screen)

        # final step
        pygame.display.flip()

    def _fire_my_bullet(self):
        new_my_bullet = MyBullet(self)
        self.mybullets.add(new_my_bullet)

    def run(self):
        while True:
            self._check_all_events()
            self._update_all_elements()
            self._draw_screen()

    def _check_solide_empty(self):
        for s in self.soliders.sprites():
            if s.rect.left < 0:
                self.soliders.empty()
                break
        if not self.soliders:
            self._fill_soliders_to_group_with_specific_rect_value()


if __name__ == "__main__":
    game = Game()
    game.run()