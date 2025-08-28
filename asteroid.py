import pygame
import random
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN, ASTEROID_MIN_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH
from circleshape import CircleShape
from powerup import PowerUp


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.rotation = 0
        self.lumpy_points = self.generate_lumpy_asteroid()

    def generate_lumpy_asteroid(self):
        points = []
        num_points = random.randint(8, 12)
        for i in range(num_points):
            angle = (360 / num_points) * i + random.uniform(-20, 20)
            distance = self.radius * random.uniform(0.7, 1.3)
            direction = pygame.Vector2(0, 1).rotate(angle)
            point = direction * distance
            points.append(point)
        return points

    def draw(self, screen):
        transformed_points = []
        for point in self.lumpy_points:
            rotated_point = point.rotate(self.rotation)
            final_point = self.position + rotated_point
            transformed_points.append(final_point)
        return pygame.draw.polygon(screen, "white", transformed_points, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT

    def split(self):
        self.kill()
        random_angle = random.uniform(20, 50)
        new_vector1 = self.velocity.rotate(random_angle)
        new_vector2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        if new_radius >= ASTEROID_MIN_RADIUS:
            new_asteroid1 = Asteroid(*self.position, new_radius)
            new_asteroid2 = Asteroid(*self.position, new_radius)
            new_asteroid1.velocity = (new_vector1 * 1.2)
            new_asteroid2.velocity = (new_vector2 * 1.2)
        else:
            return None

    def score(self, score):
        score += 1
        return score

    def remove_life(self, player_life_count):
        player_life_count -= 1
        return player_life_count

    def powerup(self):
        random_angle = random.uniform(20, 50)
        random_value = random.randrange(0, 100)
        new_vector = self.velocity.rotate(random_angle)
        if random_value in range(0, 9):
            power_up = PowerUp(*self.position, self.radius)
            power_up.velocity = (new_vector * 1.2)
        else:
            return None
