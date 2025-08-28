import pygame
import math

from constants import *

class Character():
    def __init__(self):
        self.hp = 100
        self.pos = (100, 100)# (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)
        #self.walking = {"sprite_sheet": pygame.image.load("assets/character_walking.png"), "frame_width": 32, "frame_height": 32, "frames": [pygame.Rect(i * self.walking["frame_width"], 0, self.walking["frame_width"], self.walking["frame_height"]) for i in range(5)]}
        self.image = pygame.image.load("assets/character_walking.png")
        self.frames = pygame.Rect(32, 0, 32, 32)

    def handle_events(self, game_state, event):
        pass

    def render(self, game_state):
        game_state.screen.blit(self.image, self.pos, self.frames)

    def update(self, game_state):
        dx = 0
        dy = 0
        if pygame.key.get_pressed()[pygame.K_a]:
            dx -= 64 * game_state.dt
        if pygame.key.get_pressed()[pygame.K_w]:
            dy -= 64 * game_state.dt
        if pygame.key.get_pressed()[pygame.K_d]:
            dx += 64 * game_state.dt
        if pygame.key.get_pressed()[pygame.K_s]:
            dy += 64 * game_state.dt
        if dx != 0 and dy != 0:
            length = math.sqrt(dx * dx + dy * dy)
            dx = dx * length * game_state.dt
            dy = dy * length * game_state.dt
        self.pos = (self.pos[0] + dx, self.pos[1] + dy)