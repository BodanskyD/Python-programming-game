import pygame
from game.character import Player
from game.victory import Victory
from game.scene_manager import SceneManager


class Game():

    def __init__(self, screen, level):
        self.screen = screen
        self.level = level(screen)
        self.player = Player(self.level.player_gun)
        self.camera_offset = pygame.math.Vector2(0, 0)
        self.half_width = self.screen.get_width() / 2
        self.half_height = self.screen.get_height() / 2
        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group(self.level.enemies)
        self.player_pos = pygame.Rect()
        self.walls = pygame.sprite.Group()

    def update(self, dt):

        self.calculate_camera_offset(dt)
        self.walls.empty()
        walls = self.level.update(
            (-self.camera_offset[0], -self.camera_offset[1]))
        for wall in walls:
            self.walls.add(wall)
        player_bullets = self.player.update(dt, self.player_pos.center)
        self.handle_walls(dt)
        enemy_bullets = self.handle_enemies(dt)
        self.handle_bullets(player_bullets, enemy_bullets, dt)
        self.player_pos = self.player.rotated_rect.move(self.camera_offset)
        self.screen.blit(self.player.sprite_rotated, (self.player_pos))
        if self.player.health <= 0:
            self.__init__(self.screen, type(self.level))
        else:
            for i in range(self.player.health):
                self.screen.blit(self.player.heart,
                                 (self.screen.get_width() - (i + 1) * 64,
                                  self.screen.get_height() - 100))
        if not self.enemies:
            if self.level.next_level == "victory":
                SceneManager().scene = Victory(self.screen)
            else:
                self.__init__(self.screen, self.level.next_level)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def calculate_camera_offset(self, dt):
        px, py = self.player.rotated_rect.center
        weight = pygame.math.clamp(6 * dt, 0.0, 1.0)
        mx, my = pygame.mouse.get_pos()
        mx -= self.half_width
        my -= self.half_height
        mx /= 6
        my /= 6
        self.camera_offset = pygame.math.Vector2.lerp(
            self.camera_offset,
            pygame.math.Vector2(self.half_width - px - mx,
                                self.half_height - py - my), weight)

    def handle_bullets(self, player_bullets, enemy_bullets, dt):
        if player_bullets:
            for bullet in player_bullets:
                self.player_bullets.add(bullet)
                if bullet.initial_pos == (0, 0):
                    bullet.initial_pos = (self.player_pos.center +
                                          bullet.initial_pos_offset)
                    bullet.blit_position = bullet.initial_pos
                    bullet.last_offset = (self.camera_offset)
        if enemy_bullets:
            for pos, bullet_list in enemy_bullets.items():
                if bullet_list:
                    for bullet in bullet_list:
                        self.enemy_bullets.add(bullet)
                        if bullet.initial_pos == (0, 0):
                            bullet.initial_pos = (pos +
                                                  bullet.initial_pos_offset)
                            bullet.blit_position = bullet.initial_pos
                            bullet.last_offset = (self.camera_offset)
        for bullet in self.player_bullets:
            bullet.rect = bullet.sprite.get_rect().move(bullet.blit_position)
            self.screen.blit(bullet.sprite, bullet.rect)
            bullet.update(dt, self.camera_offset)
        for bullet in self.enemy_bullets:
            bullet.rect = bullet.sprite.get_rect().move(bullet.blit_position)
            self.screen.blit(bullet.sprite, bullet.rect)
            bullet.update(dt, self.camera_offset)
        enemy_collisions = pygame.sprite.groupcollide(
            self.player_bullets, self.enemies, True, False,
            pygame.sprite.collide_rect)
        player_collisions = pygame.sprite.groupcollide(
            pygame.sprite.Group(self.player), self.enemy_bullets, False, True,
            pygame.sprite.collide_rect)
        for enemy_list in enemy_collisions.values():
            for enemy in enemy_list:
                enemy.take_damage()
        for bullet_list in player_collisions.values():
            for bullet in bullet_list:
                self.player.take_damage()

    def handle_enemies(self, dt):
        enemy_bullets = {}
        for enemy in self.enemies:
            enemy._rect = enemy.rotated_rect.move(self.camera_offset)
            enemy_bullets.update({
                enemy._rect.center:
                enemy.update(dt, enemy._rect.center, self.player_pos.center)
            })
            self.screen.blit(enemy.sprite_rotated, enemy._rect)
        return enemy_bullets

    def handle_walls(self, dt):
        self.player.rect = self.player_pos
        player_collisions = pygame.sprite.groupcollide(
            pygame.sprite.Group(self.player), self.walls, False, False,
            pygame.sprite.collide_rect)
        self.player.collide(player_collisions.values(), dt)
        for enemy in self.enemies:
            enemy.line_player = self.player.rect.clipline(
                enemy.line_start, enemy.line_end)
            if enemy.line_player:
                enemy.line_walls = [
                    x.rect.clipline(enemy.line_start, enemy.line_end)
                    for x in self.walls.sprites()
                ]
        pygame.sprite.groupcollide(self.player_bullets, self.walls, True,
                                   False, pygame.sprite.collide_rect)
        pygame.sprite.groupcollide(self.enemy_bullets, self.walls, True, False,
                                   pygame.sprite.collide_rect)
