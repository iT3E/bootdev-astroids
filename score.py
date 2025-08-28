import pygame
import random
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN, ASTEROID_MIN_RADIUS
from screentext import ScreenText


class Score(ScreenText):
    def __init__(self, x, y, radius, initial_score):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.default_score = initial_score

    def draw(self, screen):
        font = pygame.font.SysFont('arial', 30)
        number_text = font.render(
            str(self.default_score), True, (255, 255, 255))
        return screen.blit(number_text, (self.x, self.y))

    def update_text(self, new_score):
        self.default_score = new_score
