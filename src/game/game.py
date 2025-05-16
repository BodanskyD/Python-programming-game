import pygame
from game.player import Player
from game.level import Level1


class Game():

    def __init__(self, screen):
        self.screen = screen
        self.player = Player()
        self.level = Level1(screen)
        self.camera_offset = pygame.math.Vector2(0, 0)
        self.half_width = self.screen.get_width() / 2
        self.half_height = self.screen.get_height() / 2

    def update(self, dt):
        self.level.update((-self.camera_offset[0], -self.camera_offset[1]))
        self.player.update(dt, (self.half_width, self.half_height))
        self.calculate_camera_offset(dt)
        self.screen.blit(self.player.sprite_rotated,
                         (self.player.rotated_rect.move(self.camera_offset)))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def calculate_camera_offset(self, dt):
        px, py = self.player.rotated_rect.center
        weight = pygame.math.clamp(6 * dt, 0.0, 1.0)
        self.camera_offset = pygame.math.Vector2.lerp(
            self.camera_offset,
            pygame.math.Vector2(self.half_width - px, self.half_height - py),
            weight)
        # self.camera_offset = (self.half_width - px, self.half_height - py)
