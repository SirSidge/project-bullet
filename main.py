import pygame

from constants import *
from game_state import Game_State
#from scenes.buttons import Button
from scenes.main_menu import Main_Menu

pygame.init()

# Create surfaces
logic_surface = pygame.Surface((BASE_WIDTH, BASE_HEIGHT))
display_surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# Initialize game state
game_state = Game_State(logic_surface)

pygame.display.set_caption("Project Bullet")

while game_state.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state.running = False
        game_state.handle_events()

    game_state.render()

    # Scale logic surface to display surface
    pygame.transform.scale(logic_surface, (DISPLAY_WIDTH, DISPLAY_HEIGHT), display_surface)

    # Update display
    pygame.display.flip()
pygame.quit()