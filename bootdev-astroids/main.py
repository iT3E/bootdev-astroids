import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(
        f"""
    Starting Asteroids!
    Screen width: {SCREEN_WIDTH}
    Screen height: {SCREEN_HEIGHT}
        """
    )
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen
        pygame.Surface.fill(screen, color="black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
