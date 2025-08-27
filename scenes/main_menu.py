import pygame

from constants import *
from scenes.buttons import Button

class Main_Menu():
    def __init__(self):
        start_button = Button(START_BUTTON_DEST, START_BUTTON_LOC, START_BUTTON_SIZE, "start")
        quit_button = Button(QUIT_BUTTON_DEST, QUIT_BUTTON_LOC, QUIT_BUTTON_SIZE, "quit")
        self.buttons = {start_button, quit_button}
        self.wallpaper = pygame.image.load("assets/main_menu/main_menu.png")

    def render(self, game_state):
        game_state.screen.blit(self.wallpaper, (0, 0))
        for button in self.buttons:
            game_state.screen.blit(button.button_sheet, button.dest, button.off_rect if button.hover else button.on_rect)

    def handle_events(self, game_state):
        for button in self.buttons:
            if button.collision():
                button.hover = True
                if pygame.mouse.get_pressed()[0] == 1:
                    button.clicked = True
                elif pygame.mouse.get_pressed()[0] == 0 and button.clicked: #take action once button lifted after being pressed
                    if button.name == "quit":
                        game_state.running = False
                    if button.name == "start":
                        game_state.current = "game"
            else:
                button.hover = False
                button.clicked = False