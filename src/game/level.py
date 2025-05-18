import pygame
from importlib import resources as impresources
from game.character import Enemy


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,
                                        cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Tiles(metaclass=Singleton):

    def __init__(self):
        self.tile_img = pygame.image.load(
            impresources.files("game.assets") / "tiles" /
            "hotline_miami_floor.png").convert_alpha()

        self.tiles = {}

    def index_tiles(self, i):
        if i not in self.tiles:
            j, i = divmod(i, 12)
            self.tiles[i] = pygame.transform.scale_by(
                pygame.Surface.subsurface(self.tile_img, (i * 16, j * 16),
                                          (16, 16)), 4)
        return self.tiles[i]


class Tile(pygame.sprite.Sprite):

    def __init__(self, image_idx, tile_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = Tiles().index_tiles(image_idx)
        self.rect = self.image.get_rect()
        # walls: 140, 141, 142, 143
        self.idx = image_idx
        # types: 0 = floor, 1 = wall
        self.tile_type = tile_type


class Level1:

    def __init__(self, screen):
        self.enemies = [Enemy((12, 12))]
        self.fill_tile = 2
        self.tilemap = {
            (0, 0): (Tile(12, 0), ),
            (0, 2): (Tile(19, 0), ),
            (4, 5): (Tile(25, 0), Tile(140, 1)),
            (5, 5): (Tile(25, 0), Tile(141, 1)),
            (6, 6): (Tile(25, 0), Tile(142, 1)),
            (6, 7): (Tile(25, 0), Tile(143, 1)),
        }
        self.screen = screen
        self.max_x = self.screen.get_width() // 64 + 1
        self.max_y = self.screen.get_height() // 64 + 1

    def update(self, camera_offset):
        walls = []
        self.screen.fill((0, 0, 0))
        x, y = camera_offset[0] / 64, camera_offset[1] / 64
        for i in range(int(x) - 1, int(x) + self.max_x + 1):
            for j in range(int(y) - 1, int(y) + self.max_y + 1):
                if (i, j) in self.tilemap:
                    tile_list = self.tilemap[(i, j)]
                else:
                    tile_list = {Tile(self.fill_tile, 0)}
                for tile in tile_list:
                    tile.rect = pygame.Rect((i - x) * 64, (j - y) * 64, 64, 64)
                    if tile.tile_type == 1:
                        walls.append(tile)
                    self.screen.blit(Tiles().index_tiles(tile.idx), tile.rect)

        return walls
