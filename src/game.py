import sys

import pygame

from src.config import Config


class Game(object):
    def __init__(self, display):
        self.display = display
        self.config = Config()

    def loop(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            clock.tick(self.config.fps)
