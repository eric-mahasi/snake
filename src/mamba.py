import pygame

from src.config import Config


class Mamba(object):
    """A class that is used to create instances of the snake.

    ...

    Attributes
    ----------
    x_pos : int
        cartesian x-coordinate of the x position of the snake.
    y_pos : int
        cartesian y-coordinate for the y position of the snake.
    body : array_like
        a list of tuples that describe the position of different parts
        of the snake's body.
    max_size : int
        the maximum size the snake is allowed to be. Dictated by the
        number of apples the snake has eaten.
    drawn_mamba : object
        pygame object for storing rectangular coordinates of the snake.

    Methods
    -------
    eat
        Consume an apple.
    draw_body
        Display the new body part of the snake.
    draw
        Display the snake onto the screen.
    move
        Change the position of the snake on the screen.
    """

    def __init__(self, display):
        """
        Parameters
        ----------
        display : A reference to the display.
        """
        self.config = Config()
        self.display = display
        self.x_pos = int(self.config.game_width / 1.5)
        self.y_pos = int(self.config.game_height / 3)
        self.body = []
        self.max_size = 0

    def eat(self):
        """Consume an apple."""
        self.max_size += 1

    def draw_body(self):
        """Display the new body part of the snake.

        Once an apple has been eaten, draw the new body part that
        results onto the screen.
        """
        for item in self.body:
            body_rect = pygame.Rect(item[0], item[1], self.config.snake_width,
                                    self.config.snake_height)
            pygame.draw.rect(self.display, self.config.green,
                             body_rect)

    def draw(self):
        """Draw the snake onto the screen.

        Returns
        -------
        drawn_mamba : A rectangle shape for the snake.
        """
        self.mamba_rect = pygame.Rect(self.x_pos, self.y_pos,
                                      self.config.snake_width,
                                      self.config.snake_height)
        drawn_mamba = pygame.draw.rect(self.display, self.config.green,
                                       self.mamba_rect)
        return drawn_mamba

    def move(self, x_change, y_change):
        """Change the position of the snake on the screen.

        Parameters
        ----------
        x_change : int
            The change in the x direction of the snake.
        y_change : int
            The change in the y direction of the snake.
        """
        self.body.append((self.x_pos, self.y_pos))
        self.x_pos += x_change
        self.y_pos += y_change

        if len(self.body) > self.max_size:
            del (self.body[0])
