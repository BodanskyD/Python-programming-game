import pygame
import math
import src.game.assets as assets
from importlib import resources as impresources


class Player():

    def __init__(self):
        # self.player_sheet = pygame.image.load(
        #     "assets/character/player_sheet_outline.png").convert_alpha()
        self.player_sheet = pygame.image.load(
            impresources.files(assets) / 'character' /
            'player_sheet_outline.png').convert_alpha()
        self.factor = 4
        self.sprite = self.index_sheet(0)
        self.direction = pygame.Vector2()
        self.position = (0, 0)
        self.speed = 4
        # self.pistol = pygame.transform.scale_by(
        #     pygame.image.load("assets/character/pistol.png").convert_alpha(),
        #     self.factor)
        self.pistol = pygame.transform.scale_by(
            pygame.image.load(
                impresources.files(assets) / 'character' /
                'pistol.png').convert_alpha(), self.factor)
        # self.m16 = pygame.transform.scale_by(
        #     pygame.image.load(
        #         "assets/character/m16-smaller.png").convert_alpha(),
        #     self.factor)
        self.m16 = pygame.transform.scale_by(
            pygame.image.load(
                impresources.files(assets) / 'character' /
                'm16-smaller.png').convert_alpha(), self.factor)
        self.gun = self.m16
        self.sprite_index = 0
        self.animation_speed = 1 / 6
        self.walking = False

    # used https://stackoverflow.com/a/54714144
    def calculate_rotation(self):
        mouse_pos = pygame.mouse.get_pos()
        x, y, = self.sprite.get_rect(center=self.position).center
        nx, ny = x - mouse_pos[0], mouse_pos[1] - y
        angle = math.degrees(math.atan2(ny, nx)) + 90
        self.sprite_rotated = pygame.transform.rotate(self.sprite, angle)
        self.rotated_rect = self.sprite_rotated.get_rect(
            center=self.sprite.get_rect(center=(x, y)).center)

    def handle_gun(self):
        if self.gun is None:
            if self.walking:
                self.sprite_index = self.sprite_index + self.animation_speed
                self.sprite = self.index_sheet(int(self.sprite_index) % 9 + 3)
            else:
                self.sprite_index = 0
                self.sprite = self.index_sheet(self.sprite_index)
            self.speed = 5
        if self.gun == self.pistol:
            if self.walking:
                self.sprite_index = self.sprite_index + self.animation_speed
                self.sprite = self.index_sheet(int(self.sprite_index) % 9 + 27)
            else:
                self.sprite_index = 24
                self.sprite = self.index_sheet(self.sprite_index)
            self.sprite.blit(self.pistol, (0, -50))
            self.speed = 5
        if self.gun == self.m16:
            if self.walking:
                self.sprite_index = self.sprite_index + self.animation_speed
                self.sprite = self.index_sheet(int(self.sprite_index) % 9 + 15)
            else:
                self.sprite_index = 13
                self.sprite = self.index_sheet(self.sprite_index)
            self.sprite.blit(self.m16, (0, -50))
            self.speed = 4

    def index_sheet(self, i):
        return pygame.transform.scale_by(
            pygame.Surface.subsurface(self.player_sheet, (i * 64, 0),
                                      (64, 64)), self.factor)

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        self.direction = pygame.Vector2()
        self.walking = False
        if keys[pygame.K_w]:
            self.direction += pygame.Vector2(0, -1)
            self.walking = True
        if keys[pygame.K_a]:
            self.direction += pygame.Vector2(-1, 0)
            self.walking = True
        if keys[pygame.K_s]:
            self.direction += pygame.Vector2(0, 1)
            self.walking = True
        if keys[pygame.K_d]:
            self.direction += pygame.Vector2(1, 0)
            self.walking = True
        if keys[pygame.K_q]:
            self.gun = None
            self.sprite_index = 0

        if self.direction != pygame.Vector2():
            self.position += self.direction.normalize() * self.speed

    def update(self):
        self.handle_gun()
        self.calculate_rotation()
        self.handle_keys()
