import pygame


class MenuItem(pygame.sprite.Sprite):

    def __init__(self, surface, screen, text="", x=0, y=0, color=(0, 0, 0)):
        pygame.sprite.Sprite.__init__(self)

        self.image = surface
        self.rect = self.image.get_rect(center=(x, y))
        self.font = pygame.font.Font(
            "assets/gravity_pixel_font/GravityBold8.ttf", size=24)

        self.text = text
        self.hovered = False
        self.clicked = False
        self.screen = screen
        self.color = color

    def handle_mouse(self):
        self.clicked = False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hovered = True
            if pygame.mouse.get_pressed()[0]:
                self.handle_click()
        else:
            self.hovered = False

    def handle_click(self):
        self.clicked = True

    def render_text(self):
        size = self.font.size(self.text)
        position = (self.image.get_width() / 2 - size[0] / 2,
                    self.image.get_height() / 2 - size[1] / 2)
        self.image.blit(self.font.render(self.text, False, (255, 255, 255)),
                        position)

    def render(self):
        self.image.fill(self.color)
        self.render_text()
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.handle_mouse()
        self.render()
