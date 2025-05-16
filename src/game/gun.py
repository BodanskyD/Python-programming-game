import pygame
from importlib import resources as impresources
from abc import ABC


class Gun(ABC):

    def __init__(self, factor, sprite_str, offset_y, speed, walk_offset,
                 char_sprite_num, rpm):
        self.sprite = pygame.transform.scale_by(
            pygame.image.load(
                impresources.files('game.assets') / 'character' /
                sprite_str).convert_alpha(), factor)
        self.offset = (0, offset_y * factor)
        self.speed = speed
        self.walk_offset = walk_offset
        self.char_sprite_num = char_sprite_num
        self.rpm = rpm

    def shoot(self, angle):
        pass


class M16(Gun):

    def __init__(self, factor):
        super().__init__(factor, "m16-smaller.png", -12, 300, 15, 13, 420)


class Pistol(Gun):

    def __init__(self, factor):
        super().__init__(factor, "pistol.png", -12, 360, 27, 24, 180)


class Fist:

    def __init__(self):
        self.sprite = None
        self.speed = 360
        self.walk_offset = 3
        self.char_sprite_num = 0

    def shoot(self, angle):
        pass
