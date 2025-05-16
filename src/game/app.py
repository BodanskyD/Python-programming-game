import pygame
from game.main_menu import MainMenu
from game.scene_manager import SceneManager
import sys
from importlib import resources as impresources


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720), pygame.SCALED)

    clock = pygame.time.Clock()
    running = True

    # crosshair = pygame.image.load("assets/crosshair/crosshair.png")
    crosshair = pygame.image.load(
        impresources.files('game.assets') / 'crosshair' / 'crosshair.png')
    crosshair.convert()
    crosshair.set_colorkey((0, 0, 0))
    cursor = pygame.cursors.Cursor((16, 16), crosshair)
    pygame.mouse.set_cursor(cursor)
    SceneManager(MainMenu(screen))

    while running:
        pygame.display.set_caption(str(clock.get_fps()))

        scene = SceneManager().scene

        running = scene.update(clock.get_time()/1000)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
