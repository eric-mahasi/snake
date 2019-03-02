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
            pygame.font.init()
            font = pygame.font.SysFont("bitstreamveraserif", 28)
            score_text = f"Score: {self.score}"
            score = font.render(score_text, True, self.config.white)
            score_rect = pygame.Rect(self.config.game_height - 140,
                                     self.config.game_width - 30, 100, 100)
            self.display.blit(score, score_rect)
            pygame.display.update()
            clock.tick(self.config.fps)
