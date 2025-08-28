import pygame
from circleshape import CircleShape


class Bomb(CircleShape):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.initial_radius = radius
        self.is_detonated = False
        self.detonation_timer = 0
        self.max_detonation_time = 2.0
        self.max_radius = 50
        self.arm_timer = 1

    def draw(self, screen):
        return pygame.draw.circle(screen, self.color, self.position, self.radius)

    def update(self, dt):
        if self.arm_timer > 0:
            self.arm_timer -= dt

        if not self.is_detonated:
            self.position += (self.velocity * dt)
        else:
            self.detonation_timer += dt
            progress = self.detonation_timer / self.max_detonation_time
            if progress <= 1.0:
                self.radius = self.initial_radius + \
                    (self.max_radius - self.initial_radius) * progress
            else:
                self.kill()

    def detonate(self):
        if not self.is_detonated:
            self.is_detonated = True
            self.velocity = pygame.Vector2(0, 0)

    def can_detonate(self):
        return self.arm_timer <= 0
