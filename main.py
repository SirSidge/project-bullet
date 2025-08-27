import pygame

from constants import *
from game_state import Game_State
from scenes.buttons import Button

pygame.init()

# Initialize game state
game_state = Game_State()

# Create surfaces
logic_surface = pygame.Surface((BASE_WIDTH, BASE_HEIGHT))
display_surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# Load Scenes
main_menu = pygame.image.load("assets/main_menu/main_menu.png")
game = pygame.image.load("assets/Grass.png")

# Load Buttons
start_button = Button(START_BUTTON_DEST, START_BUTTON_LOC, START_BUTTON_SIZE, "start")
quit_button = Button(QUIT_BUTTON_DEST, QUIT_BUTTON_LOC, QUIT_BUTTON_SIZE, "quit") # (dest, loc, size)
buttons = {start_button, quit_button}

# Render Buttons
def Render(buttons):
    for button in buttons:
        logic_surface.blit(button.button_sheet, button.dest, button.off_rect if button.hover else button.on_rect)

pygame.display.set_caption("Project Bullet")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_state.current == "main menu":
            for button in buttons:
                if button.collision():
                    button.hover = True
                    if pygame.mouse.get_pressed()[0] == 1:
                        button.clicked = True
                    elif pygame.mouse.get_pressed()[0] == 0 and button.clicked: #take action once button lifted after being pressed
                        if button.name == "quit":
                            running = False
                        if button.name == "start":
                            game_state.current = "game"
                else:
                    button.hover = False
                    button.clicked = False

    # Clear logic surface (paint black)
    logic_surface.fill((0, 0, 0))

    # Draw main menu in native (Base resolution)
    if game_state.current == "main menu":
        logic_surface.blit(main_menu, (0, 0))
        Render(buttons)
    elif game_state.current == "game":
        logic_surface.blit(game, (0, 0))
    
    # Scale logic surface to display surface
    pygame.transform.scale(logic_surface, (DISPLAY_WIDTH, DISPLAY_HEIGHT), display_surface)

    # Update display
    pygame.display.flip()
pygame.quit()