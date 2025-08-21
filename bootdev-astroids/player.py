import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN, PLAYER_BOOST_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = PLAYER_SHOOT_COOLDOWN
        self.player_speed = PLAYER_SPEED

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        return pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
        if keys[pygame.K_RSHIFT] or keys[pygame.K_LSHIFT]:
            self.boost()
        else:
            self.deboost()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.player_speed * dt
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT

    def shoot(self, dt):
        if self.timer <= 0:
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            shot.velocity = forward * PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN

    def boost(self):
        self.player_speed = PLAYER_BOOST_SPEED

    def deboost(self):
        self.player_speed = PLAYER_SPEED
