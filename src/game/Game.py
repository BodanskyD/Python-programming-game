import pygame
from src.game.Player import Player


class Game():

    def __init__(self, screen):
        self.screen = screen
        self.player = Player()
        # self.level

    def update(self):
        self.screen.fill((128, 0, 0))
        self.player.update()
        self.screen.blit(self.player.sprite_rotated, self.player.rotated_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
