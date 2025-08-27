import pygame

from scenes.main_menu import Main_Menu

class Game_State():
    def __init__(self, logic_surface):
        self.main_menu = Main_Menu()
        self.game = pygame.image.load("assets/Grass.png")
        self.current = "main menu"
        self.previous = ""
        self.running = True
        self.screen = logic_surface
    
    def render(self):
        self.screen.fill((0, 0, 0))
        if self.current == "main menu":
            self.main_menu.render(self)
        elif self.current == "game":
            self.screen.blit(self.game, (0, 0))

    def handle_events(self):
        if self.current == "main menu":
            self.main_menu.handle_events(self)