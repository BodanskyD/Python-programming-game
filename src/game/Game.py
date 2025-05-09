import pygame
import math


class Game():

    def __init__(self, screen):
        self.screen = screen
        # self.level
        self.player_sheet = pygame.image.load(
            "assets/character/player_sheet_outline.png").convert()
        self.factor = 4
        self.player = self.index_sheet(0)

    def update(self):
        self.calculate_rotation()
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.player_rotated, self.rotated_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    # used https://stackoverflow.com/a/54714144
    def calculate_rotation(self):
        mouse_pos = pygame.mouse.get_pos()
        x, y, = self.player.get_rect().center
        nx, ny = x - mouse_pos[0], mouse_pos[1] - y
        angle = math.degrees(math.atan2(ny, nx)) + 90
        self.player_rotated = pygame.transform.rotate(self.player, angle)
        self.rotated_rect = self.player_rotated.get_rect(
            center=self.player.get_rect(center=(x, y)).center)

    def index_sheet(self, i):
        return pygame.transform.scale_by(
            pygame.Surface.subsurface(self.player_sheet, (i * 64, 0),
                                      (64, 64)), self.factor)
