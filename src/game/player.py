import pygame
import math
from importlib import resources as impresources
from game.gun import Pistol, M16, Fist


class Player():

    def __init__(self):
        self.player_sheet = pygame.image.load(
            impresources.files('game.assets') / 'character' /
            'player_sheet_outline.png').convert_alpha()
        self.factor = 4
        self.sprite = self.index_sheet(0)
        self.direction = pygame.Vector2()
        self.position = (0, 0)
        self.speed = 4
        self.pistol = Pistol(self.factor)
        self.m16 = M16(self.factor)
        self.fist = Fist()
        self.gun = self.m16
        self.sprite_index = 0
        self.animation_speed = 1 / 6
        self.angle = 0
        self.walking = False

    # used https://stackoverflow.com/a/54714144
    def calculate_rotation(self):
        mouse_pos = pygame.mouse.get_pos()
        x, y, = self.sprite.get_rect(center=self.position).center
        nx, ny = x - mouse_pos[0], mouse_pos[1] - y
        self.angle = math.degrees(math.atan2(ny, nx)) + 90
        self.sprite_rotated = pygame.transform.rotate(self.sprite, self.angle)
        self.rotated_rect = self.sprite_rotated.get_rect(
            center=self.sprite.get_rect(center=(x, y)).center)

    def handle_sprite(self):
        if self.walking:
            self.sprite_index = self.sprite_index + self.animation_speed
            self.sprite = self.index_sheet(
                int(self.sprite_index) % 9 + self.gun.walk_offset)
        else:
            self.sprite_index = self.gun.char_sprite_num
            self.sprite = self.index_sheet(self.sprite_index)
        if self.gun.sprite:
            self.sprite.blit(self.gun.sprite, self.gun.offset)
        self.speed = self.gun.speed

    def index_sheet(self, i):
        return pygame.transform.scale_by(
            pygame.Surface.subsurface(self.player_sheet, (i * 64, 0),
                                      (64, 64)), self.factor)

    def handle_attack(self):
        if pygame.mouse.get_pressed()[0]:
            self.gun.shoot(self.angle)

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        self.direction = pygame.Vector2()
        self.walking = False
        if keys[pygame.K_w]:
            self.direction += pygame.Vector2(0, -1)
        if keys[pygame.K_a]:
            self.direction += pygame.Vector2(-1, 0)
        if keys[pygame.K_s]:
            self.direction += pygame.Vector2(0, 1)
        if keys[pygame.K_d]:
            self.direction += pygame.Vector2(1, 0)
        if keys[pygame.K_q]:
            self.gun = self.fist
            self.sprite_index = 0

        if self.direction != pygame.Vector2():
            self.walking = True
            self.position += self.direction.normalize() * self.speed

    def update(self):
        self.handle_sprite()
        self.handle_attack()
        self.calculate_rotation()
        self.handle_keys()
