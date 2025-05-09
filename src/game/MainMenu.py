import pygame
from Menu import MenuItem
import SceneManager
from Game import Game


class MainMenu():

    def __init__(self, screen):
        self.screen = screen
        SCREEN_WIDTH, SCREEN_HEIGHT = self.screen.get_width(
        ), self.screen.get_height()
        x, y = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        offset = 100
        start = MenuItem(pygame.Surface((300, 80)), screen, "Start Game", x,
                         y - offset, (0, 255, 0))
        close = MenuItem(pygame.Surface((300, 80)), screen, "Quit Game", x,
                         y + offset, (255, 0, 0))
        self.menu = pygame.sprite.Group()
        self.menu.add(start)
        self.menu.add(close)

    def update(self):
        if self.menu.sprites()[0].clicked:
            SceneManager.SceneManager().set_scene(Game(self.screen))
        self.screen.fill((0, 0, 0))
        self.menu.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return not self.menu.sprites()[1].clicked
