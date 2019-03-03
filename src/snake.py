import pygame

from src.config import Config
from src.game import Game

config = Config()


def main():
    """Basic window setup."""
    display = pygame.display.set_mode((config.game_height, config.game_width))
    pygame.display.set_caption(config.game_caption)
    game = Game(display)
    game.loop()


if __name__ == '__main__':
    main()
