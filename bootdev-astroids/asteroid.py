import pygame
import random
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN, ASTEROID_MIN_RADIUS
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        random_angle = random.uniform(20, 50)
        new_vector1 = self.velocity.rotate(random_angle)
        new_vector2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        if self.radius >= ASTEROID_MIN_RADIUS:
            new_asteroid1 = Asteroid(*self.position, new_radius)
            new_asteroid2 = Asteroid(*self.position, new_radius)
            new_asteroid1.velocity = (new_vector1 * 1.2)
            new_asteroid2.velocity = (new_vector2 * 1.2)
        else:
            return

    def score(self, score):
        score += 1
        return score
