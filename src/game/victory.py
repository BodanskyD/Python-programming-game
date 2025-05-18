import pygame
from importlib import resources as impresources


class Victory():

    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(
            impresources.files('game.assets') / 'gravity_pixel_font' /
            'GravityBold8.ttf')

    def update(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        self.screen.fill((0, 0, 0))
        size = self.font.size("You Won!")
        position = (self.screen.get_width() / 2 - size[0] / 2,
                    self.screen.get_height() / 2 - size[1] / 2)
        self.screen.blit(self.font.render("You Won!", False, (255, 255, 255)),
                         position)
        return True
