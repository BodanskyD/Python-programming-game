import pygame
from game.scene_manager import SceneManager
from game.game import Game
from importlib import resources as impresources


class MenuItem(pygame.sprite.Sprite):

    def __init__(self, surface, screen, text="", x=0, y=0, color=(0, 0, 0)):
        pygame.sprite.Sprite.__init__(self)

        self.image = surface
        self.rect = self.image.get_rect(center=(x, y))
        # self.font = pygame.font.Font(
        #     "assets/gravity_pixel_font/GravityBold8.ttf", size=24)
        self.font = pygame.font.Font(
            impresources.files('game.assets') / 'gravity_pixel_font' /
            'GravityBold8.ttf')

        self.text = text
        self.hovered = False
        self.clicked = False
        self.screen = screen
        self.color = color

    def handle_mouse(self):
        self.clicked = False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hovered = True
            if pygame.mouse.get_pressed()[0]:
                self.handle_click()
        else:
            self.hovered = False

    def handle_click(self):
        self.clicked = True

    def render_text(self):
        size = self.font.size(self.text)
        position = (self.image.get_width() / 2 - size[0] / 2,
                    self.image.get_height() / 2 - size[1] / 2)
        self.image.blit(self.font.render(self.text, False, (255, 255, 255)),
                        position)

    def render(self):
        self.image.fill(self.color)
        self.render_text()
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.handle_mouse()
        self.render()


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
            SceneManager().scene = Game(self.screen)
        self.screen.fill((0, 0, 0))
        self.menu.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return not self.menu.sprites()[1].clicked
