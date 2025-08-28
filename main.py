import pygame

from constants import *
from game_state import Game_State

pygame.init()

# Create surfaces
logic_surface = pygame.Surface((BASE_WIDTH, BASE_HEIGHT))
display_surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# Initialize game state
game_state = Game_State(logic_surface)

pygame.display.set_caption("Project Bullet")

while game_state.running:
    game_state.dt = game_state.clock.tick(60) / 1000
    game_state.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state.running = False
        game_state.handle_events(event)

    game_state.render()

    # Scale logic surface to display surface
    pygame.transform.scale(logic_surface, (DISPLAY_WIDTH, DISPLAY_HEIGHT), display_surface)

    # Update display
    pygame.display.flip()
pygame.quit()