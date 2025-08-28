import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN, PLAYER_BOOST_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT
from circleshape import CircleShape
from shot import Shot
from bomb import Bomb


class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = PLAYER_SHOOT_COOLDOWN
        self.player_speed = PLAYER_SPEED
        self.shot_type = "DEFAULT"
        self.shot_modifier = "DEFAULT"
        self.shot_weapon = "DEFAULT"
        self.player_shoot_cooldown = 0.3
        self.player_bomb_cooldown = 3
        self.active_bomb = None
        self.mouse_was_pressed = False

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
        mouse = pygame.mouse.get_pressed()
        self.timer -= dt
        mouse_clicked = mouse[2] and not self.mouse_was_pressed

        if mouse_clicked and self.active_bomb is None:
            self.drop_bomb(dt)
        elif mouse_clicked and self.active_bomb and not self.active_bomb.is_detonated:
            self.active_bomb.detonate()
            self.active_bomb = None

        self.mouse_was_pressed = mouse[2]

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

        if self.active_bomb and not self.active_bomb.alive():
            self.active_bomb = None

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
            if self.shot_weapon == "SHOTGUN":
                self.shot_weapon_shotgun()
            elif self.shot_weapon == "LASERGUN":
                self.shot_weapon_lasergun()
            else:
                self.shot_weapon_default()

    def drop_bomb(self, dt):
        if self.timer <= 0 and self.active_bomb is None:
            self.active_bomb = self.bomb_default()
        # if self.bomb_one == "BOMBONE":
        #     self.bomb_one_shotgun()
        # elif self.bomb_two == "BOMBTWO":
        #     self.bomb_two_lasergun()
        # else:
        #     self.bomb_default()

    def bomb_default(self):
        bomb = Bomb(self.position.x, self.position.y, 10, "purple")
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        bomb.velocity = forward * (PLAYER_SHOOT_SPEED - 400)
        self.timer = self.player_bomb_cooldown
        return bomb

    def shot_weapon_lasergun(self):
        shot = Shot((self.position.x),
                    (self.position.y), SHOT_RADIUS, "yellow")
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
        self.timer = 0

    def shot_weapon_shotgun(self):
        shot = Shot((self.position.x),
                    (self.position.y), SHOT_RADIUS, "orange")
        shot2 = Shot((self.position.x - 5),
                     (self.position.y - 5), SHOT_RADIUS, "orange")
        shot3 = Shot((self.position.x + 5),
                     (self.position.y + 5), SHOT_RADIUS, "orange")
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        forward2 = pygame.Vector2(0, 1).rotate(self.rotation - 10)
        forward3 = pygame.Vector2(0, 1).rotate(self.rotation + 10)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
        shot2.velocity = forward2 * PLAYER_SHOOT_SPEED
        shot3.velocity = forward3 * PLAYER_SHOOT_SPEED
        self.timer = self.player_shoot_cooldown

    def shot_weapon_default(self):
        shot = Shot((self.position.x),
                    (self.position.y), SHOT_RADIUS, "red")
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
        self.timer = self.player_shoot_cooldown

    def boost(self):
        self.player_speed = PLAYER_BOOST_SPEED

    def deboost(self):
        self.player_speed = PLAYER_SPEED

    def set_shotgun(self):
        self.shot_type = "SHOTGUN"
        self.shot_weapon = "SHOTGUN"

    def set_lasergun(self):
        self.shot_type = "LASERGUN"
        self.shot_weapon = "LASERGUN"

    def set_shotspeedincrease(self):
        if self.player_shoot_cooldown > 0.1:
            self.player_shoot_cooldown -= 0.1
