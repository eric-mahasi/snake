class Config(object):
    """A class that stores all the settings that will be used globally
    throughout the game."""

    def __init__(self):
        self.game_caption = "Snake"
        self.game_height = 800
        self.game_width = 600
        self.fps = 30
        self.snake_height = 20
        self.snake_width = 20
        self.snake_speed = 5
        self.apple_width = 20
        self.apple_height = 20
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.green = (0, 100, 0)
        self.red = (100, 0, 0)
