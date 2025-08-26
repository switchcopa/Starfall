import pygame
from game import Game 
from config import WINDOW_WIDTH, WINDOW_HEIGHT


black = (0,0,0)
game = Game(black, 'Starfall', WINDOW_WIDTH, WINDOW_HEIGHT) 
game.run()
