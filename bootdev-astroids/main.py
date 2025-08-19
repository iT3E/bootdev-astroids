import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from score import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    group_updatable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()
    group_asteroids = pygame.sprite.Group()
    group_shots = pygame.sprite.Group()
    Score.containers = (group_drawable, group_shots)
    Shot.containers = (group_shots, group_updatable, group_drawable)
    AsteroidField.containers = (group_updatable,)
    Asteroid.containers = (group_asteroids, group_updatable, group_drawable)
    Player.containers = (group_updatable, group_drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    game_score_display = Score(100, 100, 2, score)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for i in group_drawable:
            i.draw(screen)
        group_updatable.update(dt)
        for i in group_asteroids:
            if i.col_check(player) == True:
                return print("Game over!")
                sys.exit[0]
            for s in group_shots:
                if s.col_check(i) == True:
                    s.kill()
                    i.split()
                    score = i.score(score)
                    game_score_display.update_score(score)
                    print(f"Score:{score}")

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
