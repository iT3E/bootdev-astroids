import pygame
import random
from circleshape import CircleShape


class PowerUp(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        return pygame.draw.circle(screen, "green", self.position, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def poweruptype(self, player):
        random_value = random.randrange(0, 29)
        if random_value in range(0, 9):
            return self.shotspeedincrease(player)
        if random_value in range(10, 19):
            return self.shotgun(player)
        if random_value in range(20, 29):
            return self.lasergun(player)
        # if random_value in range(31, 40):
        #     return shieldboost

    def shotgun(self, player):
        print("Shotgun!")
        player.set_shotgun()

    def lasergun(self, player):
        print("Lasergun!")
        player.set_lasergun()

    def shotspeedincrease(self, player):
        print("Increase Speed!")
        player.set_shotspeedincrease()

        # def speedshoot():
        #     return None
        #
        # def shieldboost():
        #     return None
