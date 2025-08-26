import pygame
from src.core.game import Game 
from src.core.config import WINDOW_WIDTH, WINDOW_HEIGHT

pygame.init()

black = (0,0,0)
game = Game(black, 'Starfall', WINDOW_WIDTH, WINDOW_HEIGHT) 
game.run()
