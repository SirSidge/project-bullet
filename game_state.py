import pygame

from scenes.main_menu import Main_Menu
from scenes.character import Character

class Game_State():
    def __init__(self, logic_surface):
        self.main_menu = Main_Menu()
        self.character = Character()
        self.game = pygame.image.load("assets/Grass.png")
        self.current = "main menu"
        self.previous = ""
        self.running = True
        self.screen = logic_surface
        self.clock = pygame.time.Clock()
        self.dt = 0
    
    def render(self):
        self.screen.fill((0, 0, 0))
        if self.current == "main menu":
            self.main_menu.render(self)
        elif self.current == "game":
            self.screen.blit(self.game, (0, 0))
            self.character.render(self)

    def handle_events(self, event):
        if self.current == "main menu":
            self.main_menu.handle_events(self, event)
        if self.current == "game":
            self.character.handle_events(self, event)

    def update(self):
        if self.current == "game":
            self.character.update(self)