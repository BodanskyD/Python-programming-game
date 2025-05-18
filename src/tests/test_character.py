import unittest
import pygame
from game.gun import Pistol, M16, Fist
from game.character import Character, Player, Enemy

class TestCharacter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pygame.init()
        cls.screen = pygame.display.set_mode((800, 600))

    @classmethod
    def tearDownClass(cls):
        pygame.quit()

    def setUp(self):
        self.character = Character('player_sheet_outline.png', (100, 100))

    def test_initialization(self):
        self.assertEqual(self.character.position, (100, 100))
        self.assertEqual(self.character.health, 3)
        self.assertIsInstance(self.character.gun, Pistol)

    def test_take_damage(self):
        self.character.take_damage()
        self.assertEqual(self.character.health, 2)
        self.character.take_damage()
        self.character.take_damage()
        self.assertEqual(self.character.health, 0)

    def test_calculate_rotation(self):
        self.character.calculate_rotation((200, 200), (150, 150))
        self.assertIsInstance(self.character.sprite_rotated, pygame.Surface)

    def test_handle_sprite(self):
        dt = 0.1
        self.character.walking = True
        initial_sprite = self.character.sprite
        self.character.handle_sprite(dt)
        self.assertNotEqual(self.character.sprite, initial_sprite)

class TestPlayer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pygame.init()
        cls.screen = pygame.display.set_mode((800, 600))

    @classmethod
    def tearDownClass(cls):
        pygame.quit()

    def setUp(self):
        self.player = Player(gun="m16")

    def test_initialization(self):
        self.assertIsInstance(self.player.gun, M16)
        self.assertEqual(self.player.health, 3)


class TestEnemy(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pygame.init()
        cls.screen = pygame.display.set_mode((800, 600))

    @classmethod
    def tearDownClass(cls):
        pygame.quit()

    def setUp(self):
        self.enemy = Enemy((200, 200), weapon="pistol")

    def test_initialization(self):
        self.assertIsInstance(self.enemy.gun, Pistol)

    def test_handle_attack(self):
        self.enemy.line_player = [(100, 100), (200, 200)]
        bullets = self.enemy.handle_attack()
        self.assertIsNotNone(bullets)

    def test_update(self):
        dt = 0.1
        center = (300, 300)
        target = (250, 250)
        self.enemy.update(dt, center, target)
        self.assertIsInstance(self.enemy.sprite_rotated, pygame.Surface)

if __name__ == '__main__':
    unittest.main()
