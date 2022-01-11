import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import Game_Stats
from button import Button
# from score_board import Scoreboard


class AlienInvasion:
    '''Overall class to manage game assets and behavior.'''

    def __init__(self):
        '''Initialize the game, and create game resources. '''
        pygame.init()
        self.settings = Settings()
        self._set_game_screen()
        self._add_elements_to_game()
        # self._create_fleet()


    def _set_game_screen(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

    def _add_elements_to_game(self):
        # elements of the game
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.button = Button(self, "Play Now", 80)
        self.button_up = Button(self, "Upgrade", -80)

        self.stats = Game_Stats(self)
        # self.scoreboard = Scoreboard(self)

    def run_game(self):
        '''Start the main loop for the game'''
        while 1: # to constantly run the game till quit -> NOTE: 1 is faster than True
            self._check_event()
            if self.stats.game_active:
                # remove button
                self.button.show_button = False
                self.button_up.show_button = False
                self._update_elements()
            else:
                # add button
                self.button.show_button = True
                self.button_up.show_button = True
                # self._reset_screen()
                self.aliens.empty()
                self.bullets.empty()
                self._create_fleet()
                self.ship.recenter()
                pygame.mouse.set_visible(True)
            self._update_screen()

    def _check_event(self):
        # Watch for keyboard and mouse events.
        # set_allowed to avoid checking on other events
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYUP, pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN])
        for event in pygame.event.get():  # returns a list of events that have taken place since the last time this function was called
            if event.type == pygame.QUIT :
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    self._check_play_button(mouse_position)


    def _update_elements(self):
        self.ship.update()
        self._update_bullets()
        self._update_aliens()

    def _update_screen(self):
        ''' for dynamically draw all elements'''
        # design the screen - background and elements
        self.screen.fill(self.settings.bg_color)
        # after background painted, paint the following in order
        self.ship.blitme()
        # update bullets
        for b in self.bullets.sprites(): # type(b) is bullet(Bullet)
            '''NOTE: .sprites() can be removed, no change'''
            b.draw_bullet() # although this method is not recognized in code, but in game the group is filled with Bullet instances.

        # draw fleet of aliens altogether
        self.aliens.draw(self.screen)

        # draw scoreboard
        # self.scoreboard.show_scoreboard()

        # show or no-show button
        if self.button.show_button:
            self.button.button_appear()
        if self.button_up.show_button:
            self.button_up.button_appear()

        # Make the most recently drawn screen visible.
        pygame.display.flip()  # Update the full display Surface to the screen

    def _update_bullets(self):
        self.bullets.update()# this will auto call each bullet of its update()
        self._remove_run_away_bullet()

        # check collision ****TODO: update the score here
        bullet_dic = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        # for bullet in bullet_dic.keys():
        #     for alien in bullet_dic[bullet]:
        #         self.stats.score += self.settings.score_scale
        # self.scoreboard.update_score()


    def _remove_run_away_bullet(self):
        # remove run_away bullets
        for b in self.bullets.copy():  # type(b) is bullet(Bullet), ALSO, use a copy() to loop thru the list so that we can change itself during the loop
            if b.rect.bottom < 0:
                self.bullets.remove(b)

    def _check_keydown_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True  # flag
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            # create a new bullet and fire
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        # only allow 3 bullets exist anytime at most
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        # create one alien to get all values needed from it
        new_alien = Alien(self)
        alien_width, alien_height = new_alien.rect.size  # one line defines two values
        numbers_allowed_horizontal = (self.screen.get_width() - (2 * alien_width)) // (2 * alien_width)
        numbers_allowed_vertical = (self.screen.get_height() - (3 * alien_height) - self.ship.rect.height) // (
                    2 * alien_height)
        for row in range(numbers_allowed_vertical):
            for col in range(numbers_allowed_horizontal):
                alien = Alien(self)
                # use float instead , alien.rect.x can be integer only
                alien.x = alien_width + col * 2 * alien_width
                alien.y = alien_height + row * 2 * alien_height
                alien.rect.x = alien.x
                alien.rect.y = alien.y
                self.aliens.add(alien)


    def _update_aliens(self):
        # move to the edge
        self.aliens.update()
        self._check_alien_to_edge()
        self._check_alien_fleet_empty()
        self._check_ship_hit_alien()
        self._check_alien_touch_bottom()

    def _check_alien_fleet_empty(self):
        if not self.aliens:
            self._create_fleet()
            self.bullets.empty()
            self.settings.speed_up_game() #TODO: level up / speed up /

    def _check_alien_touch_bottom(self):
        for a in self.aliens.sprites():
            if a.rect.bottom > self.screen.get_height()+ 30:
                text = 'touch bottom'
                self._ship_hit(text)
                break

    def _check_ship_hit_alien(self):
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            text = 'hit ship'
            self._ship_hit(text)

    def _check_alien_to_edge(self):
        for alien in self.aliens.sprites():
            if alien.check_edge():
                # whole fleet drop and change direction
                self._alien_fleet_drop_and_change_direction()
                break

    def _alien_fleet_drop_and_change_direction(self):
        for alien in self.aliens.sprites():
            alien.speed *= (-1)
            alien.rect.y += self.settings.alien_drop_speed

    def _ship_hit(self, text):
        if self.stats.ship_left > 0:
            self.stats.ship_left -= 1
            # self._reset_screen()
            self.aliens.empty()
            self.bullets.empty()
            self.ship.recenter()
            sleep(0.5)
            # self._create_fleet()

        else:
            self.stats.game_active = False
            self.stats.ship_left = self.settings.ship_limit

    def _reset_screen(self):
            # remove all aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            # recenter the ship
            self.ship.recenter()

    def _check_play_button(self, mouse_position):
        button_clicked = self.button.rect.collidepoint(mouse_position)
        button_up_clicked = self.button_up.rect.collidepoint(mouse_position)
        if button_clicked and not self.stats.game_active:
            self._turn_on_game()
            self.settings.reset_speed()

        if button_up_clicked and not self.stats.game_active:
            self._turn_on_game()
            self.settings.reset_higher_speed()

    def _turn_on_game(self):
        self.stats.game_active = True
        pygame.mouse.set_visible(False)


if __name__ == '__main__':
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
