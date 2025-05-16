import pygame
from importlib import resources as impresources


class Level1:

    def __init__(self, screen):
        self.tile_img = pygame.image.load(
            impresources.files("game.assets") / "tiles" /
            "hotline_miami_floor.png").convert_alpha()
        self.tiles = {}
        self.fill_tile = 2
        self.tilemap = {(0, 0): 12, (0, 2): 19, (5, 5): 141, (6, 5): 142}
        self.screen = screen
        self.max_x = self.screen.get_width() // 64 + 1
        self.max_y = self.screen.get_height() // 64 + 1

    def update(self, camera_offset):
        self.screen.fill((0, 0, 0))
        x, y = camera_offset[0] / 64, camera_offset[1] / 64
        for i in range(int(x) - 1, int(x) + self.max_x + 1):
            for j in range(int(y) - 1, int(y) + self.max_y + 1):
                if (i, j) in self.tilemap:
                    tile_idx = self.tilemap[(i, j)]
                else:
                    tile_idx = self.fill_tile
                # print(camera_offset)
                if tile_idx in (140, 141, 142, 143):
                    self.screen.blit(self.index_tiles(self.fill_tile),
                                     ((i - x) * 64, (j - y) * 64))
                self.screen.blit(self.index_tiles(tile_idx),
                                 ((i - x) * 64, (j - y) * 64))

    def index_tiles(self, i):
        if i not in self.tiles:
            j, i = divmod(i, 12)
            self.tiles[i] = pygame.transform.scale_by(
                pygame.Surface.subsurface(self.tile_img, (i * 16, j * 16),
                                          (16, 16)), 4)
        return self.tiles[i]
