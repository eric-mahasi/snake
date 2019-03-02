import sys

import pygame

from src.config import Config


class Game(object):
    def __init__(self, display):
        self.display = display
        self.config = Config()

    def loop(self):
        clock = pygame.time.Clock()
        x_change = 0
        y_change = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -self.config.snake_speed
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = self.config.snake_speed
                    y_change = 0
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = self.config.snake_speed
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -self.config.snake_speed

            self.display.fill(self.config.black)
            self.mamba.move(x_change, y_change)
            self.mamba.draw()
            pygame.display.update()
            clock.tick(self.config.fps)
