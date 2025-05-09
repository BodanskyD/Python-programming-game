import pygame
from MainMenu import MainMenu
from SceneManager import SceneManager
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720), pygame.SCALED)

    clock = pygame.time.Clock()
    running = True

    crosshair = pygame.image.load("assets/crosshair/crosshair.png")
    crosshair.convert()
    crosshair.set_colorkey((0, 0, 0))
    cursor = pygame.cursors.Cursor((16, 16), crosshair)
    pygame.mouse.set_cursor(cursor)
    SceneManager(MainMenu(screen))

    while running:

        scene = SceneManager().get_scene()

        running = scene.update()

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
