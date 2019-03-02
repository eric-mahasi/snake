import pygame

from src.config import Config


class Mamba(object):
    def __init__(self, display):
        self.config = Config()
        self.display = display
        self.x_pos = int(self.config.game_width / 1.5)
        self.y_pos = int(self.config.game_height / 3)
        self.body = []
        self.max_size = 0

    def eat(self):
        self.max_size += 1

    def draw_body(self):
        for item in self.body:
            body_rect = pygame.Rect(item[0], item[1], self.config.snake_width,
                                    self.config.snake_height)
            pygame.draw.rect(self.display, self.config.green, body_rect)

    def draw(self):
        self.mamba_rect = pygame.Rect(self.x_pos, self.y_pos,
                                      self.config.snake_width,
                                      self.config.snake_height)
        drawn_mamba = pygame.draw.rect(self.display, self.config.green,
                                       self.mamba_rect)
        return drawn_mamba

    def move(self, x_change, y_change):
        self.body.append((self.x_pos, self.y_pos))
        self.x_pos += x_change
        self.y_pos += y_change

        if len(self.body) > self.max_size:
            del (self.body[0])
