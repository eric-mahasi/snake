import random

import pygame

from src.config import Config


class Apple:
    """A class that handles creation of apples for the snake to eat.

    ...

    Attributes
    ----------
    x_pos : int
        cartesian x-coordinate of the x position of the apple.
    y_pos : int
        cartesian y-coordinate of the y position of the apple.
    apple_rect : object
        pygame object for storing rectangular coordinates of the apple.

    Methods
    -------
    randomize
        Generate a new apple at a random point on the screen.
    draw
        Display the apple onto the screen.
    """

    def __init__(self, display):
        """
        Parameters
        ----------
        display : A reference to the display.
        """
        self.display = display
        self.x_pos = 0
        self.y_pos = 0
        self.config = Config()
        self.randomize()

    def randomize(self):
        """Generate a new apple at a random point on the screen."""
        height = self.config.game_height
        width = self.config.game_width
        max_x = height - self.config.snake_width
        max_y = width - self.config.snake_height
        self.x_pos = random.randint(30, max_x)
        self.y_pos = random.randint(30, max_y)

    def draw(self):
        """Display the apple onto the screen.

        Returns
        -------
        drawn_apple : A rectangle shape for the apple.
        """
        self.apple_rect = pygame.Rect(self.x_pos, self.y_pos,
                                      self.config.apple_height,
                                      self.config.apple_width)
        drawn_apple = pygame.draw.rect(self.display, self.config.red,
                                       self.apple_rect)
        return drawn_apple
