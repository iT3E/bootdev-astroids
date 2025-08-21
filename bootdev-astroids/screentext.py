import pygame
import random
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN, ASTEROID_MIN_RADIUS
from circleshape import CircleShape


class ScreenText(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # super().__init__(x, y, radius)
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.x = x
        self.y = y
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        font = pygame.font.SysFont('arial', 30)
        number_text = font.render(
            str(self.default_score), True, (255, 255, 255))
        return screen.blit(number_text, (self.x, self.y))

    def update_text(self, new_text):
        pass
