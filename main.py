import pygame

pygame.init()

# Base resolutiuon
BASE_WIDTH, BASE_HEIGHT = 320, 180
# Display resolution
DISPLAY_WIDTH, DISPLAY_HEIGHT = 1280, 720
SCALE_FACTOR = DISPLAY_WIDTH // BASE_WIDTH

# Create surfaces
logic_surface = pygame.Surface((BASE_WIDTH, BASE_HEIGHT))
display_surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# Load main menu
main_menu = pygame.image.load("assets/main-menu/main-menu.png")

#screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Project Bullet")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Clear logic surface (paint black)
    logic_surface.fill((0, 0, 0))

    # Draw main menu in native (Base resolution)
    logic_surface.blit(main_menu, (0, 0))

    # Scale logic surface to display surface
    pygame.transform.scale(logic_surface, (DISPLAY_WIDTH, DISPLAY_HEIGHT), display_surface)

    # Update display
    pygame.display.flip()
pygame.quit()