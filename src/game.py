import sys

import pygame

from src.config import Config
from src.apple import Apple
from src.mamba import Mamba


class Game(object):
    """A class that creates the main game loop.

    ...

    Attributes
    ----------
    score : int
        the score that the player has earned. It is simply the number of
        apples that the snake has eaten.
    """

    def __init__(self, display):
        """
        Parameters
        ----------
        display : A reference to the display.
        """
        self.display = display
        self.config = Config()
        self.apple = Apple(display)
        self.mamba = Mamba(display)
        self.score = 0

    def loop(self):
        """The main loop of the game."""
        global event
        clock = pygame.time.Clock()
        x_change = 0
        y_change = 0
        # This infinite while loop continually detects arrow key inputs
        # from the user and refreshes and updates the displayed images.
        # The loop exits when the user closes the game window.
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

            # Displaying the screen, the snake and the apple onto it.
            self.display.fill(self.config.black)
            self.apple.draw()
            self.mamba.move(x_change, y_change)
            self.mamba.draw()
            self.mamba.eat()

            # Checking whether the snake has hit the apple. If that
            # happens, eat the apple, generate a new one and increase
            # the score.
            if self.apple.apple_rect.colliderect(self.mamba.mamba_rect):
                self.apple.randomize()
                self.score += 1

            # Printing the score text onto the screen
            pygame.font.init()
            font = pygame.font.SysFont("bitstreamveraserif", 28)
            score_text = f"Score: {self.score}"
            score = font.render(score_text, True, self.config.white)
            score_rect = pygame.Rect(self.config.game_height - 140,
                                     self.config.game_width - 30, 100, 100)
            self.display.blit(score, score_rect)

            pygame.display.update()
            clock.tick(self.config.fps)
