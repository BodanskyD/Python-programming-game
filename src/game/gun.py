import pygame
from importlib import resources as impresources
from abc import ABC
import random


class Bullet(pygame.sprite.Sprite):

    def __init__(self, factor, angle, offset):
        pygame.sprite.Sprite.__init__(self)
        self._sprite = pygame.transform.scale_by(
            pygame.image.load(
                impresources.files('game.assets') / 'character' /
                'bullet.png'), factor).convert_alpha()
        self.image = self._sprite
        self.rect = self._sprite.get_rect()
        self.initial_pos = pygame.math.Vector2(0, 0)
        self.last_offset = (0, 0)
        # self.position = self.initial_pos
        self.blit_position = (0, 0)
        self.lifetime = 0.0
        self.angle = angle
        self.direction = pygame.math.Vector2(0, -1).rotate(-angle)
        self.initial_pos_offset = self.direction * (offset * factor)
        self.speed = 800
        self.max_life = 2.0

    @property
    def sprite(self):
        x, y, = self._sprite.get_rect().center
        self.sprite_rotated = pygame.transform.rotate(self._sprite, self.angle)
        self.rotated_rect = self.sprite_rotated.get_rect(
            center=self._sprite.get_rect(center=(x, y)).center)
        self.image = self.sprite_rotated
        return self.sprite_rotated

    def update(self, dt, camera_offset):
        self.lifetime += dt
        if self.lifetime >= self.max_life:
            pygame.sprite.Sprite.kill(self)
        move = (self.direction.normalize() * self.speed * dt)
        self.blit_position = (self.blit_position[0] + move[0]) - (
            self.last_offset[0] - camera_offset[0]), (
                self.blit_position[1] + move[1]) - (self.last_offset[1] -
                                                    camera_offset[1])
        self.last_offset = camera_offset


class Gun(ABC):

    def __init__(self, factor, sprite_str, offset_y, speed, walk_offset,
                 char_sprite_num, rpm, spread, bullet_offset):
        self.sprite = pygame.transform.scale_by(
            pygame.image.load(
                impresources.files('game.assets') / 'character' /
                sprite_str).convert_alpha(), factor)
        self.offset = (0, offset_y * factor)
        self.factor = factor
        self.speed = speed
        self.walk_offset = walk_offset
        self.char_sprite_num = char_sprite_num
        self.rpm = rpm
        self.bullets = []
        self.timer = 0.0
        self.spread = spread
        self.bullet_offset = bullet_offset

    def shoot(self, angle):
        self.bullets = []
        if self.timer >= 60 / self.rpm:
            spread = (random.random() - 0.5) * self.spread
            self.bullets.append(
                Bullet(self.factor, angle + spread, self.bullet_offset))
            self.timer = 0.0
        return self.bullets

    def update(self, dt):
        self.timer += dt


class M16(Gun):

    def __init__(self, factor):
        super().__init__(factor, "m16-smaller.png", -12, 300, 15, 13, 720, 14,
                         28)


class Pistol(Gun):

    def __init__(self, factor):
        super().__init__(factor, "pistol.png", -12, 360, 27, 24, 180, 4, 16)


class Fist:

    def __init__(self):
        self.sprite = None
        self.speed = 360
        self.walk_offset = 3
        self.char_sprite_num = 0

    def shoot(self, angle):
        pass

    def update(self, dt):
        pass
