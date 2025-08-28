import pygame
from circleshape import CircleShape


class Bomb(CircleShape):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, screen):
        return pygame.draw.circle(screen, self.color, self.position, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
