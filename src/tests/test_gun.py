import unittest
import pygame
import math
from unittest.mock import patch, MagicMock
import os
import sys
from pygame.math import Vector2
from game.gun import Bullet, Gun, M16, Pistol, Fist

class TestGun(unittest.TestCase):
    
    def setUp(self):
        pygame.init()
        
        self.image_mock = MagicMock()
        self.image_mock.convert_alpha.return_value = pygame.Surface((10, 10))
        
        self.patcher = patch('pygame.image.load', return_value=self.image_mock)
        self.mock_load = self.patcher.start()
        
        self.resources_patcher = patch('importlib.resources.files')
        self.mock_resources = self.resources_patcher.start()
        self.mock_resources.return_value = MagicMock()
        
        self.factor = 2
        self.sprite_str = "test_gun.png"
        self.offset_y = -10
        self.speed = 300
        self.walk_offset = 15
        self.char_sprite_num = 10
        self.rpm = 600
        self.spread = 10
        self.bullet_offset = 20
    
    def tearDown(self):

        self.patcher.stop()
        self.resources_patcher.stop()
        pygame.quit()
    
    def test_gun_initialization(self):
        gun = Gun(self.factor, self.sprite_str, self.offset_y, self.speed, 
                  self.walk_offset, self.char_sprite_num, self.rpm, self.spread, 
                  self.bullet_offset)
        
        self.assertEqual(gun.factor, self.factor)
        self.assertEqual(gun.offset, (0, self.offset_y * self.factor))
        self.assertEqual(gun.speed, self.speed)
        self.assertEqual(gun.walk_offset, self.walk_offset)
        self.assertEqual(gun.char_sprite_num, self.char_sprite_num)
        self.assertEqual(gun.rpm, self.rpm)
        self.assertEqual(gun.spread, self.spread)
        self.assertEqual(gun.bullet_offset, self.bullet_offset)
        self.assertEqual(gun.timer, 0.0)
        self.assertEqual(gun.bullets, [])
    
    def test_gun_update(self):
        gun = Gun(self.factor, self.sprite_str, self.offset_y, self.speed, 
                  self.walk_offset, self.char_sprite_num, self.rpm, self.spread, 
                  self.bullet_offset)
        
        dt = 0.1
        gun.update(dt)
        self.assertEqual(gun.timer, dt)
        
        gun.update(dt)
        self.assertEqual(gun.timer, dt * 2)
    
    @patch('random.random', return_value=0.5)
    def test_gun_shoot_with_timer_ready(self, mock_random):
        gun = Gun(self.factor, self.sprite_str, self.offset_y, self.speed, 
                  self.walk_offset, self.char_sprite_num, self.rpm, self.spread, 
                  self.bullet_offset)
        
        gun.timer = 60 / gun.rpm + 0.1
        angle = 30
        
        with patch('game.gun.Bullet') as mock_bullet:
            bullet_instance = MagicMock()
            mock_bullet.return_value = bullet_instance
            
            bullets = gun.shoot(angle)
            
            mock_bullet.assert_called_once_with(self.factor, angle, self.bullet_offset)
            self.assertEqual(bullets, [bullet_instance])
            self.assertEqual(gun.timer, 0.0)
    
    @patch('random.random', return_value=0.5)
    def test_gun_shoot_with_spread(self, mock_random):
        gun = Gun(self.factor, self.sprite_str, self.offset_y, self.speed, 
                  self.walk_offset, self.char_sprite_num, self.rpm, self.spread, 
                  self.bullet_offset)
        
        gun.timer = 60 / gun.rpm + 0.1
        angle = 30
        
        expected_spread = (0.5 - 0.5) * gun.spread
        
        with patch('game.gun.Bullet') as mock_bullet:
            gun.shoot(angle)
            
            mock_bullet.assert_called_once_with(self.factor, angle + expected_spread, self.bullet_offset)
    
    def test_gun_shoot_with_timer_not_ready(self):
        gun = Gun(self.factor, self.sprite_str, self.offset_y, self.speed, 
                  self.walk_offset, self.char_sprite_num, self.rpm, self.spread, 
                  self.bullet_offset)
        
        gun.timer = 60 / gun.rpm - 0.1
        angle = 30
        
        with patch('game.gun.Bullet') as mock_bullet:
            bullets = gun.shoot(angle)
            
            mock_bullet.assert_not_called()
            self.assertEqual(bullets, [])
            self.assertAlmostEqual(gun.timer, 60 / gun.rpm - 0.1)


class TestSpecificGuns(unittest.TestCase):
    
    def setUp(self):
        pygame.init()
        
        self.image_mock = MagicMock()
        self.image_mock.convert_alpha.return_value = pygame.Surface((10, 10))
        
        self.patcher = patch('pygame.image.load', return_value=self.image_mock)
        self.mock_load = self.patcher.start()
        
        self.resources_patcher = patch('importlib.resources.files')
        self.mock_resources = self.resources_patcher.start()
        self.mock_resources.return_value = MagicMock()
        
        self.factor = 2
    
    def tearDown(self):
        self.patcher.stop()
        self.resources_patcher.stop()
        pygame.quit()
    
    def test_m16_initialization(self):
        m16 = M16(self.factor)
        
        self.assertEqual(m16.factor, self.factor)
        self.assertEqual(m16.offset, (0, -12 * self.factor))
        self.assertEqual(m16.speed, 300)
        self.assertEqual(m16.walk_offset, 15)
        self.assertEqual(m16.char_sprite_num, 13)
        self.assertEqual(m16.rpm, 720)
        self.assertEqual(m16.spread, 14)
        self.assertEqual(m16.bullet_offset, 28)
        
        self.mock_resources.assert_called()
        self.mock_load.assert_called_once()
    
    def test_pistol_initialization(self):
        pistol = Pistol(self.factor)
        
        self.assertEqual(pistol.factor, self.factor)
        self.assertEqual(pistol.offset, (0, -12 * self.factor))
        self.assertEqual(pistol.speed, 360)
        self.assertEqual(pistol.walk_offset, 27)
        self.assertEqual(pistol.char_sprite_num, 24)
        self.assertEqual(pistol.rpm, 180)
        self.assertEqual(pistol.spread, 4)
        self.assertEqual(pistol.bullet_offset, 16)
        
        self.mock_resources.assert_called()
        self.mock_load.assert_called_once()


class TestFist(unittest.TestCase):
    
    def test_fist_initialization(self):
        fist = Fist()
        
        self.assertIsNone(fist.sprite)
        self.assertEqual(fist.speed, 360)
        self.assertEqual(fist.walk_offset, 3)
        self.assertEqual(fist.char_sprite_num, 0)
    
    def test_fist_shoot(self):
        fist = Fist()
        result = fist.shoot(45)
        self.assertIsNone(result)
    
    def test_fist_update(self):
        fist = Fist()
        fist.update(0.1)


if __name__ == "__main__":
    unittest.main()
