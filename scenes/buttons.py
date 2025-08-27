import pygame

from constants import SCALE_FACTOR

button_sheet = pygame.image.load("assets/buttons.png")
button_width = 48 # Each button grid is 48x16, size can be smaller but not bigger

class Button():
    def __init__(self, dest, loc, size, name):
        self.dest = dest
        self.off_rect = pygame.Rect(loc[0], loc[1], size[0], size[1])
        self.on_rect = pygame.Rect(loc[0] + 48, loc[1], size[0], size[1])
        self.button_sheet = button_sheet
        self.clicked = False
        self.hover = False
        self.name = name

    def collision(self):
        return pygame.Rect.collidepoint(pygame.rect.Rect(self.dest[0] * SCALE_FACTOR, self.dest[1] * SCALE_FACTOR, self.off_rect[2] * SCALE_FACTOR, self.off_rect[3] * SCALE_FACTOR), pygame.mouse.get_pos())