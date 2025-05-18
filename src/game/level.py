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


class BaseLevel():

    def __init__(self, base):
        self.tilemap = {
            (0, 0): (),
            (0, 1): (Tile(141, 1), ),
            (0, 2): (Tile(141, 1), ),
            (0, 3): (Tile(141, 1), ),
            (0, 4): (Tile(141, 1), ),
            (0, 5): (Tile(141, 1), ),
            (0, 6): (Tile(141, 1), ),
            (0, 7): (Tile(141, 1), ),
            (0, 8): (Tile(141, 1), ),
            (0, 9): (Tile(141, 1), ),
            (0, 10): (Tile(141, 1), ),
            (0, 11): (Tile(141, 1), ),
            (0, 12): (Tile(141, 1), ),
            (0, 13): (Tile(141, 1), ),
            (0, 14): (Tile(141, 1), ),
            (0, 15): (Tile(141, 1), ),
            (0, 16): (Tile(141, 1), ),
            (0, 17): (Tile(141, 1), ),
            (0, 18): (Tile(141, 1), ),
            (0, 19): (),
            (1, 0): (Tile(143, 1), ),
            (1, 1): (Tile(base, 0), ),
            (1, 2): (Tile(base, 0), ),
            (1, 3): (Tile(base, 0), ),
            (1, 4): (Tile(base, 0), ),
            (1, 5): (Tile(base, 0), ),
            (1, 6): (Tile(base, 0), ),
            (1, 7): (Tile(base, 0), ),
            (1, 8): (Tile(base, 0), ),
            (1, 9): (Tile(base, 0), ),
            (1, 10): (Tile(base, 0), ),
            (1, 11): (Tile(base, 0), ),
            (1, 12): (Tile(base, 0), ),
            (1, 13): (Tile(base, 0), ),
            (1, 14): (Tile(base, 0), ),
            (1, 15): (Tile(base, 0), ),
            (1, 16): (Tile(base, 0), ),
            (1, 17): (Tile(base, 0), ),
            (1, 18): (Tile(base, 0), ),
            (1, 19): (Tile(142, 1), ),
            (2, 0): (Tile(143, 1), ),
            (2, 1): (Tile(base, 0), ),
            (2, 2): (Tile(base, 0), ),
            (2, 3): (Tile(base, 0), ),
            (2, 4): (Tile(base, 0), ),
            (2, 5): (Tile(base, 0), ),
            (2, 6): (Tile(base, 0), ),
            (2, 7): (Tile(base, 0), ),
            (2, 8): (Tile(base, 0), ),
            (2, 9): (Tile(base, 0), ),
            (2, 10): (Tile(base, 0), ),
            (2, 11): (Tile(base, 0), ),
            (2, 12): (Tile(base, 0), ),
            (2, 13): (Tile(base, 0), ),
            (2, 14): (Tile(base, 0), ),
            (2, 15): (Tile(base, 0), ),
            (2, 16): (Tile(base, 0), ),
            (2, 17): (Tile(base, 0), ),
            (2, 18): (Tile(base, 0), ),
            (2, 19): (Tile(142, 1), ),
            (3, 0): (Tile(143, 1), ),
            (3, 1): (Tile(base, 0), ),
            (3, 2): (Tile(base, 0), ),
            (3, 3): (Tile(base, 0), ),
            (3, 4): (Tile(base, 0), ),
            (3, 5): (Tile(base, 0), ),
            (3, 6): (Tile(base, 0), ),
            (3, 7): (Tile(base, 0), ),
            (3, 8): (Tile(base, 0), ),
            (3, 9): (Tile(base, 0), ),
            (3, 10): (Tile(base, 0), ),
            (3, 11): (Tile(base, 0), ),
            (3, 12): (Tile(base, 0), ),
            (3, 13): (Tile(base, 0), ),
            (3, 14): (Tile(base, 0), ),
            (3, 15): (Tile(base, 0), ),
            (3, 16): (Tile(base, 0), ),
            (3, 17): (Tile(base, 0), ),
            (3, 18): (Tile(base, 0), ),
            (3, 19): (Tile(142, 1), ),
            (4, 0): (Tile(143, 1), ),
            (4, 1): (Tile(base, 0), ),
            (4, 2): (Tile(base, 0), ),
            (4, 3): (Tile(base, 0), ),
            (4, 4): (Tile(base, 0), ),
            (4, 5): (Tile(base, 0), ),
            (4, 6): (Tile(base, 0), ),
            (4, 7): (Tile(base, 0), ),
            (4, 8): (Tile(base, 0), ),
            (4, 9): (Tile(base, 0), ),
            (4, 10): (Tile(base, 0), ),
            (4, 11): (Tile(base, 0), ),
            (4, 12): (Tile(base, 0), ),
            (4, 13): (Tile(base, 0), ),
            (4, 14): (Tile(base, 0), ),
            (4, 15): (Tile(base, 0), ),
            (4, 16): (Tile(base, 0), ),
            (4, 17): (Tile(base, 0), ),
            (4, 18): (Tile(base, 0), ),
            (4, 19): (Tile(142, 1), ),
            (5, 0): (Tile(143, 1), ),
            (5, 1): (Tile(base, 0), ),
            (5, 2): (Tile(base, 0), ),
            (5, 3): (Tile(base, 0), ),
            (5, 4): (Tile(base, 0), ),
            (5, 5): (Tile(base, 0), ),
            (5, 6): (Tile(base, 0), ),
            (5, 7): (Tile(base, 0), ),
            (5, 8): (Tile(base, 0), ),
            (5, 9): (Tile(base, 0), ),
            (5, 10): (Tile(base, 0), ),
            (5, 11): (Tile(base, 0), ),
            (5, 12): (Tile(base, 0), ),
            (5, 13): (Tile(base, 0), ),
            (5, 14): (Tile(base, 0), ),
            (5, 15): (Tile(base, 0), ),
            (5, 16): (Tile(base, 0), ),
            (5, 17): (Tile(base, 0), ),
            (5, 18): (Tile(base, 0), ),
            (5, 19): (Tile(142, 1), ),
            (6, 0): (Tile(143, 1), ),
            (6, 1): (Tile(base, 0), ),
            (6, 2): (Tile(base, 0), ),
            (6, 3): (Tile(base, 0), ),
            (6, 4): (Tile(base, 0), ),
            (6, 5): (Tile(base, 0), ),
            (6, 6): (Tile(base, 0), ),
            (6, 7): (Tile(base, 0), ),
            (6, 8): (Tile(base, 0), ),
            (6, 9): (Tile(base, 0), ),
            (6, 10): (Tile(base, 0), ),
            (6, 11): (Tile(base, 0), ),
            (6, 12): (Tile(base, 0), ),
            (6, 13): (Tile(base, 0), ),
            (6, 14): (Tile(base, 0), ),
            (6, 15): (Tile(base, 0), ),
            (6, 16): (Tile(base, 0), ),
            (6, 17): (Tile(base, 0), ),
            (6, 18): (Tile(base, 0), ),
            (6, 19): (Tile(142, 1), ),
            (7, 0): (Tile(143, 1), ),
            (7, 1): (Tile(base, 0), ),
            (7, 2): (Tile(base, 0), ),
            (7, 3): (Tile(base, 0), ),
            (7, 4): (Tile(base, 0), ),
            (7, 5): (Tile(base, 0), ),
            (7, 6): (Tile(base, 0), ),
            (7, 7): (Tile(base, 0), ),
            (7, 8): (Tile(base, 0), ),
            (7, 9): (Tile(base, 0), ),
            (7, 10): (Tile(base, 0), ),
            (7, 11): (Tile(base, 0), ),
            (7, 12): (Tile(base, 0), ),
            (7, 13): (Tile(base, 0), ),
            (7, 14): (Tile(base, 0), ),
            (7, 15): (Tile(base, 0), ),
            (7, 16): (Tile(base, 0), ),
            (7, 17): (Tile(base, 0), ),
            (7, 18): (Tile(base, 0), ),
            (7, 19): (Tile(142, 1), ),
            (8, 0): (Tile(143, 1), ),
            (8, 1): (Tile(base, 0), ),
            (8, 2): (Tile(base, 0), ),
            (8, 3): (Tile(base, 0), ),
            (8, 4): (Tile(base, 0), ),
            (8, 5): (Tile(base, 0), ),
            (8, 6): (Tile(base, 0), ),
            (8, 7): (Tile(base, 0), ),
            (8, 8): (Tile(base, 0), ),
            (8, 9): (Tile(base, 0), ),
            (8, 10): (Tile(base, 0), ),
            (8, 11): (Tile(base, 0), ),
            (8, 12): (Tile(base, 0), ),
            (8, 13): (Tile(base, 0), ),
            (8, 14): (Tile(base, 0), ),
            (8, 15): (Tile(base, 0), ),
            (8, 16): (Tile(base, 0), ),
            (8, 17): (Tile(base, 0), ),
            (8, 18): (Tile(base, 0), ),
            (8, 19): (Tile(142, 1), ),
            (9, 0): (Tile(143, 1), ),
            (9, 1): (Tile(base, 0), ),
            (9, 2): (Tile(base, 0), ),
            (9, 3): (Tile(base, 0), ),
            (9, 4): (Tile(base, 0), ),
            (9, 5): (Tile(base, 0), ),
            (9, 6): (Tile(base, 0), ),
            (9, 7): (Tile(base, 0), ),
            (9, 8): (Tile(base, 0), ),
            (9, 9): (Tile(base, 0), ),
            (9, 10): (Tile(base, 0), ),
            (9, 11): (Tile(base, 0), ),
            (9, 12): (Tile(base, 0), ),
            (9, 13): (Tile(base, 0), ),
            (9, 14): (Tile(base, 0), ),
            (9, 15): (Tile(base, 0), ),
            (9, 16): (Tile(base, 0), ),
            (9, 17): (Tile(base, 0), ),
            (9, 18): (Tile(base, 0), ),
            (9, 19): (Tile(142, 1), ),
            (10, 0): (Tile(143, 1), ),
            (10, 1): (Tile(base, 0), ),
            (10, 2): (Tile(base, 0), ),
            (10, 3): (Tile(base, 0), ),
            (10, 4): (Tile(base, 0), ),
            (10, 5): (Tile(base, 0), ),
            (10, 6): (Tile(base, 0), ),
            (10, 7): (Tile(base, 0), ),
            (10, 8): (Tile(base, 0), ),
            (10, 9): (Tile(base, 0), ),
            (10, 10): (Tile(base, 0), ),
            (10, 11): (Tile(base, 0), ),
            (10, 12): (Tile(base, 0), ),
            (10, 13): (Tile(base, 0), ),
            (10, 14): (Tile(base, 0), ),
            (10, 15): (Tile(base, 0), ),
            (10, 16): (Tile(base, 0), ),
            (10, 17): (Tile(base, 0), ),
            (10, 18): (Tile(base, 0), ),
            (10, 19): (Tile(142, 1), ),
            (11, 0): (Tile(143, 1), ),
            (11, 1): (Tile(base, 0), ),
            (11, 2): (Tile(base, 0), ),
            (11, 3): (Tile(base, 0), ),
            (11, 4): (Tile(base, 0), ),
            (11, 5): (Tile(base, 0), ),
            (11, 6): (Tile(base, 0), ),
            (11, 7): (Tile(base, 0), ),
            (11, 8): (Tile(base, 0), ),
            (11, 9): (Tile(base, 0), ),
            (11, 10): (Tile(base, 0), ),
            (11, 11): (Tile(base, 0), ),
            (11, 12): (Tile(base, 0), ),
            (11, 13): (Tile(base, 0), ),
            (11, 14): (Tile(base, 0), ),
            (11, 15): (Tile(base, 0), ),
            (11, 16): (Tile(base, 0), ),
            (11, 17): (Tile(base, 0), ),
            (11, 18): (Tile(base, 0), ),
            (11, 19): (Tile(142, 1), ),
            (12, 0): (Tile(143, 1), ),
            (12, 1): (Tile(base, 0), ),
            (12, 2): (Tile(base, 0), ),
            (12, 3): (Tile(base, 0), ),
            (12, 4): (Tile(base, 0), ),
            (12, 5): (Tile(base, 0), ),
            (12, 6): (Tile(base, 0), ),
            (12, 7): (Tile(base, 0), ),
            (12, 8): (Tile(base, 0), ),
            (12, 9): (Tile(base, 0), ),
            (12, 10): (Tile(base, 0), ),
            (12, 11): (Tile(base, 0), ),
            (12, 12): (Tile(base, 0), ),
            (12, 13): (Tile(base, 0), ),
            (12, 14): (Tile(base, 0), ),
            (12, 15): (Tile(base, 0), ),
            (12, 16): (Tile(base, 0), ),
            (12, 17): (Tile(base, 0), ),
            (12, 18): (Tile(base, 0), ),
            (12, 19): (Tile(142, 1), ),
            (13, 0): (Tile(143, 1), ),
            (13, 1): (Tile(base, 0), ),
            (13, 2): (Tile(base, 0), ),
            (13, 3): (Tile(base, 0), ),
            (13, 4): (Tile(base, 0), ),
            (13, 5): (Tile(base, 0), ),
            (13, 6): (Tile(base, 0), ),
            (13, 7): (Tile(base, 0), ),
            (13, 8): (Tile(base, 0), ),
            (13, 9): (Tile(base, 0), ),
            (13, 10): (Tile(base, 0), ),
            (13, 11): (Tile(base, 0), ),
            (13, 12): (Tile(base, 0), ),
            (13, 13): (Tile(base, 0), ),
            (13, 14): (Tile(base, 0), ),
            (13, 15): (Tile(base, 0), ),
            (13, 16): (Tile(base, 0), ),
            (13, 17): (Tile(base, 0), ),
            (13, 18): (Tile(base, 0), ),
            (13, 19): (Tile(142, 1), ),
            (14, 0): (Tile(143, 1), ),
            (14, 1): (Tile(base, 0), ),
            (14, 2): (Tile(base, 0), ),
            (14, 3): (Tile(base, 0), ),
            (14, 4): (Tile(base, 0), ),
            (14, 5): (Tile(base, 0), ),
            (14, 6): (Tile(base, 0), ),
            (14, 7): (Tile(base, 0), ),
            (14, 8): (Tile(base, 0), ),
            (14, 9): (Tile(base, 0), ),
            (14, 10): (Tile(base, 0), ),
            (14, 11): (Tile(base, 0), ),
            (14, 12): (Tile(base, 0), ),
            (14, 13): (Tile(base, 0), ),
            (14, 14): (Tile(base, 0), ),
            (14, 15): (Tile(base, 0), ),
            (14, 16): (Tile(base, 0), ),
            (14, 17): (Tile(base, 0), ),
            (14, 18): (Tile(base, 0), ),
            (14, 19): (Tile(142, 1), ),
            (15, 0): (Tile(143, 1), ),
            (15, 1): (Tile(base, 0), ),
            (15, 2): (Tile(base, 0), ),
            (15, 3): (Tile(base, 0), ),
            (15, 4): (Tile(base, 0), ),
            (15, 5): (Tile(base, 0), ),
            (15, 6): (Tile(base, 0), ),
            (15, 7): (Tile(base, 0), ),
            (15, 8): (Tile(base, 0), ),
            (15, 9): (Tile(base, 0), ),
            (15, 10): (Tile(base, 0), ),
            (15, 11): (Tile(base, 0), ),
            (15, 12): (Tile(base, 0), ),
            (15, 13): (Tile(base, 0), ),
            (15, 14): (Tile(base, 0), ),
            (15, 15): (Tile(base, 0), ),
            (15, 16): (Tile(base, 0), ),
            (15, 17): (Tile(base, 0), ),
            (15, 18): (Tile(base, 0), ),
            (15, 19): (Tile(142, 1), ),
            (16, 0): (Tile(143, 1), ),
            (16, 1): (Tile(base, 0), ),
            (16, 2): (Tile(base, 0), ),
            (16, 3): (Tile(base, 0), ),
            (16, 4): (Tile(base, 0), ),
            (16, 5): (Tile(base, 0), ),
            (16, 6): (Tile(base, 0), ),
            (16, 7): (Tile(base, 0), ),
            (16, 8): (Tile(base, 0), ),
            (16, 9): (Tile(base, 0), ),
            (16, 10): (Tile(base, 0), ),
            (16, 11): (Tile(base, 0), ),
            (16, 12): (Tile(base, 0), ),
            (16, 13): (Tile(base, 0), ),
            (16, 14): (Tile(base, 0), ),
            (16, 15): (Tile(base, 0), ),
            (16, 16): (Tile(base, 0), ),
            (16, 17): (Tile(base, 0), ),
            (16, 18): (Tile(base, 0), ),
            (16, 19): (Tile(142, 1), ),
            (17, 0): (Tile(143, 1), ),
            (17, 1): (Tile(base, 0), ),
            (17, 2): (Tile(base, 0), ),
            (17, 3): (Tile(base, 0), ),
            (17, 4): (Tile(base, 0), ),
            (17, 5): (Tile(base, 0), ),
            (17, 6): (Tile(base, 0), ),
            (17, 7): (Tile(base, 0), ),
            (17, 8): (Tile(base, 0), ),
            (17, 9): (Tile(base, 0), ),
            (17, 10): (Tile(base, 0), ),
            (17, 11): (Tile(base, 0), ),
            (17, 12): (Tile(base, 0), ),
            (17, 13): (Tile(base, 0), ),
            (17, 14): (Tile(base, 0), ),
            (17, 15): (Tile(base, 0), ),
            (17, 16): (Tile(base, 0), ),
            (17, 17): (Tile(base, 0), ),
            (17, 18): (Tile(base, 0), ),
            (17, 19): (Tile(142, 1), ),
            (18, 0): (Tile(143, 1), ),
            (18, 1): (Tile(base, 0), ),
            (18, 2): (Tile(base, 0), ),
            (18, 3): (Tile(base, 0), ),
            (18, 4): (Tile(base, 0), ),
            (18, 5): (Tile(base, 0), ),
            (18, 6): (Tile(base, 0), ),
            (18, 7): (Tile(base, 0), ),
            (18, 8): (Tile(base, 0), ),
            (18, 9): (Tile(base, 0), ),
            (18, 10): (Tile(base, 0), ),
            (18, 11): (Tile(base, 0), ),
            (18, 12): (Tile(base, 0), ),
            (18, 13): (Tile(base, 0), ),
            (18, 14): (Tile(base, 0), ),
            (18, 15): (Tile(base, 0), ),
            (18, 16): (Tile(base, 0), ),
            (18, 17): (Tile(base, 0), ),
            (18, 18): (Tile(base, 0), ),
            (18, 19): (Tile(142, 1), ),
            (19, 0): (),
            (19, 1): (Tile(140, 1), ),
            (19, 2): (Tile(140, 1), ),
            (19, 3): (Tile(140, 1), ),
            (19, 4): (Tile(140, 1), ),
            (19, 5): (Tile(140, 1), ),
            (19, 6): (Tile(140, 1), ),
            (19, 7): (Tile(140, 1), ),
            (19, 8): (Tile(140, 1), ),
            (19, 9): (Tile(140, 1), ),
            (19, 10): (Tile(140, 1), ),
            (19, 11): (Tile(140, 1), ),
            (19, 12): (Tile(140, 1), ),
            (19, 13): (Tile(140, 1), ),
            (19, 14): (Tile(140, 1), ),
            (19, 15): (Tile(140, 1), ),
            (19, 16): (Tile(140, 1), ),
            (19, 17): (Tile(140, 1), ),
            (19, 18): (Tile(140, 1), ),
            (19, 19): (),
        }


class Tiles(metaclass=Singleton):

    def __init__(self):
        self.tile_img = pygame.image.load(
            impresources.files("game.assets") / "tiles" /
            "hotline_miami_floor.png").convert_alpha()

        self.tiles = {}

    def index_tiles(self, i):
        if i not in self.tiles:
            j, y = divmod(i, 12)
            self.tiles[i] = pygame.transform.scale_by(
                pygame.Surface.subsurface(self.tile_img, (y * 16, j * 16),
                                          (16, 16)), 4)
        return self.tiles[i]


class Tile(pygame.sprite.Sprite):

    def __init__(self, image_idx, tile_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = Tiles().index_tiles(image_idx)
        self._rect = self.image.get_bounding_rect()
        # walls: 140, 141, 142, 143
        self.idx = image_idx
        # types: 0 = floor, 1 = wall
        self.tile_type = tile_type

    @property
    def rect(self):
        r = self.image.get_bounding_rect().fit(self._rect)
        match self.idx:
            case 140:
                return r.move(-28, 0)
            case 141:
                return self._rect
            case 142:
                return r.move(0, -28)
            case 143:
                return self._rect
            case _:
                return r

    @rect.setter
    def rect(self, r):
        self._rect = r


class Level:

    def __init__(self, screen):
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


class Level1(Level):

    def __init__(self, screen):
        super().__init__(screen)
        self.player_gun = "m16"
        self.enemies = [
            Enemy((500, 500)),
            Enemy((850, 1050)),
            Enemy((150, 1050)),
            Enemy((650, 1050))
        ]
        self.next_level = Level2
        self.fill_tile = 0
        self.tilemap = BaseLevel(157).tilemap
        self.tilemap[(6, 1)] = (
            Tile(157, 0),
            Tile(140, 1),
        )
        self.tilemap[(6, 2)] = (
            Tile(157, 0),
            Tile(140, 1),
        )
        self.tilemap[(1, 5)] = (
            Tile(157, 0),
            Tile(142, 1),
        )
        self.tilemap[(2, 5)] = (
            Tile(157, 0),
            Tile(142, 1),
        )
        self.tilemap[(3, 5)] = (
            Tile(157, 0),
            Tile(142, 1),
        )
        self.tilemap[(4, 5)] = (
            Tile(157, 0),
            Tile(142, 1),
        )
        self.tilemap[(5, 5)] = (
            Tile(157, 0),
            Tile(142, 1),
        )
        self.tilemap[(12, 13)] = (
            Tile(157, 0),
            Tile(140, 1),
        )
        self.tilemap[(12, 14)] = (
            Tile(157, 0),
            Tile(140, 1),
        )
        self.tilemap[(12, 15)] = (
            Tile(157, 0),
            Tile(140, 1),
        )
        self.tilemap[(12, 16)] = (
            Tile(157, 0),
            Tile(140, 1),
        )
        self.tilemap[(12, 17)] = (
            Tile(157, 0),
            Tile(140, 1),
        )
        self.tilemap[(12, 18)] = (
            Tile(157, 0),
            Tile(140, 1),
        )
        self.tilemap[(11, 13)] = (
            Tile(157, 0),
            Tile(142, 1),
        )
        self.tilemap[(10, 13)] = (
            Tile(157, 0),
            Tile(142, 1),
        )
        self.tilemap[(9, 13)] = (
            Tile(157, 0),
            Tile(142, 1),
        )
        self.tilemap[(8, 13)] = (
            Tile(157, 0),
            Tile(142, 1),
        )
        self.tilemap[(7, 13)] = (
            Tile(157, 0),
            Tile(142, 1),
        )
        self.tilemap[(3, 13)] = (
            Tile(157, 0),
            Tile(142, 1),
        )
        self.tilemap[(2, 13)] = (
            Tile(157, 0),
            Tile(142, 1),
        )
        self.tilemap[(1, 13)] = (
            Tile(157, 0),
            Tile(142, 1),
        )


class Level2(Level):

    def __init__(self, screen):
        super().__init__(screen)
        self.player_gun = "pistol"
        self.enemies = [
            Enemy((500, 500)),
            Enemy((850, 720)),
            Enemy((1150, 720)),
            Enemy((320, 720)),
            Enemy((950, 100), "m16"),
        ]
        self.fill_tile = 0
        self.next_level = Level3
        self.tilemap = BaseLevel(168).tilemap

        self.tilemap[(1, 4)] = (
            Tile(168, 0),
            Tile(142, 1),
        )
        self.tilemap[(2, 4)] = (
            Tile(168, 0),
            Tile(142, 1),
        )
        self.tilemap[(3, 4)] = (
            Tile(168, 0),
            Tile(142, 1),
        )
        self.tilemap[(4, 4)] = (
            Tile(168, 0),
            Tile(142, 1),
        )
        self.tilemap[(5, 4)] = (
            Tile(168, 0),
            Tile(142, 1),
        )
        self.tilemap[(6, 4)] = (
            Tile(168, 0),
            Tile(142, 1),
        )
        self.tilemap[(7, 4)] = (
            Tile(168, 0),
            Tile(142, 1),
        )
        self.tilemap[(1, 10)] = (
            Tile(168, 0),
            Tile(142, 1),
        )
        self.tilemap[(2, 10)] = (
            Tile(168, 0),
            Tile(142, 1),
        )
        self.tilemap[(3, 10)] = (
            Tile(168, 0),
            Tile(142, 1),
        )
        self.tilemap[(4, 10)] = (
            Tile(168, 0),
            Tile(142, 1),
        )
        self.tilemap[(5, 10)] = (
            Tile(168, 0),
            Tile(142, 1),
        )
        self.tilemap[(6, 10)] = (
            Tile(168, 0),
            Tile(142, 1),
        )
        self.tilemap[(7, 10)] = (
            Tile(168, 0),
            Tile(142, 1),
        )
        self.tilemap[(8, 10)] = (
            Tile(168, 0),
            Tile(142, 1),
        )
        self.tilemap[(12, 10)] = (Tile(168, 0), Tile(142, 1), Tile(140, 1))
        self.tilemap[(13, 10)] = (
            Tile(168, 0),
            Tile(142, 1),
        )
        self.tilemap[(14, 10)] = (
            Tile(168, 0),
            Tile(142, 1),
        )
        self.tilemap[(15, 10)] = (
            Tile(168, 0),
            Tile(142, 1),
        )
        self.tilemap[(16, 10)] = (
            Tile(168, 0),
            Tile(142, 1),
        )
        self.tilemap[(17, 10)] = (
            Tile(168, 0),
            Tile(142, 1),
        )
        self.tilemap[(18, 10)] = (
            Tile(168, 0),
            Tile(142, 1),
        )
        self.tilemap[(12, 11)] = (
            Tile(168, 0),
            Tile(140, 1),
        )
        self.tilemap[(12, 12)] = (
            Tile(168, 0),
            Tile(140, 1),
        )
        self.tilemap[(12, 13)] = (
            Tile(168, 0),
            Tile(140, 1),
        )
        self.tilemap[(12, 14)] = (
            Tile(168, 0),
            Tile(140, 1),
        )
        self.tilemap[(12, 1)] = (
            Tile(168, 0),
            Tile(140, 1),
        )
        self.tilemap[(12, 2)] = (
            Tile(168, 0),
            Tile(140, 1),
        )
        self.tilemap[(12, 3)] = (
            Tile(168, 0),
            Tile(140, 1),
        )
        self.tilemap[(12, 4)] = (
            Tile(168, 0),
            Tile(140, 1),
        )


class Level3(Level):

    def __init__(self, screen):
        super().__init__(screen)
        self.player_gun = "m16"
        self.enemies = [
            Enemy((900, 160), "m16"),
            Enemy((1160, 140), "m16"),
            Enemy((200, 720), "pistol"),
            Enemy((320, 900), "m16"),
            Enemy((1160, 840), "m16"),
        ]
        self.fill_tile = 0
        self.next_level = "victory"
        self.tilemap = BaseLevel(228).tilemap
        self.tilemap[(8, 4)] = (
            Tile(228, 0),
            Tile(142, 1),
        )
        self.tilemap[(9, 4)] = (
            Tile(228, 0),
            Tile(142, 1),
        )
        self.tilemap[(10, 4)] = (
            Tile(228, 0),
            Tile(142, 1),
        )
        self.tilemap[(11, 4)] = (
            Tile(228, 0),
            Tile(142, 1),
        )
        self.tilemap[(12, 4)] = (
            Tile(228, 0),
            Tile(142, 1),
        )
        self.tilemap[(13, 3)] = (
            Tile(228, 0),
            Tile(140, 1),
        )
        self.tilemap[(13, 2)] = (
            Tile(228, 0),
            Tile(140, 1),
        )
        self.tilemap[(13, 1)] = (
            Tile(228, 0),
            Tile(140, 1),
        )
        self.tilemap[(1, 9)] = (
            Tile(228, 0),
            Tile(142, 1),
        )
        self.tilemap[(2, 9)] = (
            Tile(228, 0),
            Tile(142, 1),
        )
        self.tilemap[(3, 9)] = (
            Tile(228, 0),
            Tile(142, 1),
        )
        self.tilemap[(4, 9)] = (
            Tile(228, 0),
            Tile(142, 1),
        )
        self.tilemap[(5, 9)] = (
            Tile(228, 0),
            Tile(142, 1),
        )
        self.tilemap[(6, 9)] = (
            Tile(228, 0),
            Tile(140, 1),
        )
        self.tilemap[(6, 10)] = (
            Tile(228, 0),
            Tile(140, 1),
        )
        self.tilemap[(6, 11)] = (
            Tile(228, 0),
            Tile(140, 1),
        )
        self.tilemap[(6, 12)] = (
            Tile(228, 0),
            Tile(140, 1),
        )
        self.tilemap[(6, 13)] = (
            Tile(228, 0),
            Tile(140, 1),
        )
        self.tilemap[(6, 14)] = (
            Tile(228, 0),
            Tile(140, 1),
        )
        self.tilemap[(6, 15)] = (
            Tile(228, 0),
            Tile(140, 1),
        )
        self.tilemap[(14, 6)] = (
            Tile(228, 0),
            Tile(142, 1),
        )
        self.tilemap[(15, 6)] = (
            Tile(228, 0),
            Tile(142, 1),
        )
        self.tilemap[(16, 6)] = (
            Tile(228, 0),
            Tile(142, 1),
        )
        self.tilemap[(17, 6)] = (
            Tile(228, 0),
            Tile(142, 1),
        )
        self.tilemap[(18, 6)] = (
            Tile(228, 0),
            Tile(142, 1),
        )
        self.tilemap[(4, 16)] = (
            Tile(228, 0),
            Tile(142, 1),
        )
        self.tilemap[(5, 16)] = (
            Tile(228, 0),
            Tile(142, 1),
        )
        self.tilemap[(17, 10)] = (
            Tile(228, 0),
            Tile(140, 1),
        )
        self.tilemap[(17, 11)] = (
            Tile(228, 0),
            Tile(140, 1),
        )
        self.tilemap[(17, 12)] = (
            Tile(228, 0),
            Tile(140, 1),
        )
        self.tilemap[(17, 13)] = (
            Tile(228, 0),
            Tile(140, 1),
        )
        self.tilemap[(17, 14)] = (
            Tile(228, 0),
            Tile(140, 1),
        )
        self.tilemap[(17, 15)] = (
            Tile(228, 0),
            Tile(140, 1),
        )
