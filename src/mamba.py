import pygame

from src.config import Config


class Mamba(object):
    def __init__(self, display):
        self.config = Config()
        self.display = display
        self.x_pos = int(self.config.game_width / 1.5)
        self.y_pos = int(self.config.game_height / 3)

    def draw(self):
        mamba_rect = pygame.Rect(self.x_pos, self.y_pos,
                                 self.config.snake_width,
                                 self.config.snake_height)
        pygame.draw.rect(self.display, self.config.green, mamba_rect)

    def move(self, x_change, y_change):
        self.x_pos += x_change
        self.y_pos += y_change
