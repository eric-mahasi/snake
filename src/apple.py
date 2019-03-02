import random

import pygame

from src.config import Config


class Apple:
    def __init__(self, display):
        self.display = display
        self.x_pos = 0
        self.y_pos = 0
        self.config = Config()
        self.randomize()

    def randomize(self):
        height = self.config.game_height
        width = self.config.game_width
        max_x = height - self.config.snake_width
        max_y = width - self.config.snake_height

        self.x_pos = random.randint(30, max_x)
        self.y_pos = random.randint(30, max_y)

    def draw(self):
        self.apple_rect = pygame.Rect(self.x_pos, self.y_pos,
                                      self.config.apple_height,
                                      self.config.apple_width)
        drawn_apple = pygame.draw.rect(self.display, self.config.red,
                                       self.apple_rect)
        return drawn_apple
