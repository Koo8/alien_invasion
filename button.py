import pygame
class Button:
    def __init__(self, ai_game, msg, dis):
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # draw rect as a button, with msg to appear once created
        self.width, self.height = 150, 50
        self.button_color = self.settings.button_color
        self.text_color = self.settings.text_color
        self.font = ai_game.settings.font
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self._set_center(dis)
        
        self._prep_msg(msg)
        self.show_button = True

    #Pygame works with text by rendering it as an image using font.render()
    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center =self.rect.center

    def button_appear(self):
        # fill() for create shape with color
        self.screen.fill(self.button_color, self.rect)
        # blit() for draw image at the right location
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def _set_center(self, dis):
        self.rect.center = self.screen.get_rect().center
        self.rect.x += dis


