import pygame
import math
from importlib import resources as impresources
from game.gun import Pistol, M16, Fist


class Character(pygame.sprite.Sprite):

    def __init__(self, file_name, position):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(
            impresources.files('game.assets') / 'character' /
            file_name).convert_alpha()
        self._rect = self.image.get_rect()
        self.factor = 3
        self.sprite = self.index_sheet(0)
        self.sprite_rotated = self.sprite
        self.rotated_rect = self.sprite.get_rect()
        self.direction = pygame.Vector2()
        self.position = position
        self.speed = 4
        self.pistol = Pistol(self.factor)
        self.m16 = M16(self.factor)
        self.fist = Fist()
        self.gun = self.pistol
        self.sprite_index = 0
        self.animation_speed = 12
        self.angle = 0
        self.walking = False
        self.health = 3

    @property
    def rect(self):
        return self._rect.scale_by(0.2)

    @rect.setter
    def rect(self, value):
        self._rect = value

    # used https://stackoverflow.com/a/54714144
    def calculate_rotation(self, center, target):
        x, y, = self.sprite.get_rect(center=self.position).center
        nx, ny = center[0] - target[0], target[1] - center[1]
        self.angle = math.degrees(math.atan2(ny, nx)) + 90
        self.sprite_rotated = pygame.transform.rotate(self.sprite, self.angle)
        self.rotated_rect = self.sprite_rotated.get_rect(
            center=self.sprite.get_rect(center=(x, y)).center)

    def handle_sprite(self, dt):
        if self.walking:
            self.sprite_index = self.sprite_index + (self.animation_speed * dt)
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
            pygame.Surface.subsurface(self.image, (i * 64, 0), (64, 64)),
            self.factor)

    def handle_attack(self):
        pass

    def update(self, dt, center):
        self.handle_sprite(dt)
        self.gun.update(dt)
        bullets = self.handle_attack()
        return bullets

    def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            pygame.sprite.Sprite.kill(self)


class Player(Character):

    def __init__(self, gun="pistol"):
        super().__init__('player_sheet_outline.png', (200, 200))
        if gun == "pistol":
            self.gun = self.pistol
        elif gun == "m16":
            self.gun = self.m16
        self.heart = pygame.transform.scale_by(pygame.image.load(
            impresources.files('game.assets') / 'character' /
            'heart.png').convert_alpha(), 3)

    def handle_attack(self):
        if pygame.mouse.get_pressed()[0]:
            bullets = self.gun.shoot(self.angle)
            return bullets

    def handle_keys(self, dt):
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
        # if keys[pygame.K_q]:
        #     self.gun = self.fist
        #     self.sprite_index = 0

        if self.direction != pygame.Vector2():
            self.walking = True
            self.position += self.direction.normalize() * self.speed * dt

    def update(self, dt, center):
        self.handle_keys(dt)
        self.calculate_rotation(center, pygame.mouse.get_pos())
        return super().update(dt, center)

    def collide(self, walls, dt):
        if walls:
            for wall_list in walls:
                for wall in wall_list:
                    if self.direction != pygame.Vector2():
                        self.position -= (self.direction.normalize() *
                                          self.speed * dt) * 1.5
                        self.direction = pygame.Vector2(0, 0)


class Enemy(Character):

    def __init__(self, position, weapon="pistol"):
        super().__init__('enemy_sheet.png', position)
        if weapon == "pistol":
            self.gun = self.pistol
        elif weapon == "m16":
            self.gun = self.m16
        else:
            self.gun = self.fist
        self.line_start = pygame.Vector2(self._rect.center)
        self.line_end = (0, 0)
        self.line_walls = []
        self.line_player = []
        self.last_player_pos = (0, 0)
        self.position = pygame.Vector2(self.position)

    def handle_attack(self):
        shoot = False
        if self.line_player:
            shoot = True
            line_player_start, _ = self.line_player
            for line_wall in self.line_walls:
                if line_wall:
                    line_wall_start, _ = line_wall
                    if self.line_start.distance_to(
                            line_wall_start) < self.line_start.distance_to(
                                line_player_start):
                        shoot = False
        start_x, start_y = self._rect.center
        end_x, end_y = pygame.Vector2(0, -1).rotate(-self.angle) * 500
        end_x += start_x
        end_y += start_y
        self.line_start = pygame.Vector2(start_x, start_y)
        self.line_end = (end_x, end_y)
        if shoot:
            return self.gun.shoot(self.angle)

    def update(self, dt, center, target):
        self.calculate_rotation(center, target)
        return super().update(dt, center)
