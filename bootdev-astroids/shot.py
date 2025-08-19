import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN, ASTEROID_MIN_RADIUS
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
