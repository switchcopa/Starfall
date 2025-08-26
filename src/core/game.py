import pygame 
from config import WINDOW_WIDTH, WINDOW_HEIGHT

class Game: 
    def __init__(self, background_color, caption, window_width, window_height): 
        self.background_color = background_color 
        self.caption = caption
        self.screen_width = window_width
        self.screen_height = window_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

    def run(self): 
        pygame.display.set_caption(self.caption)
        self.screen.fill(self.background_color) 

        pygame.display.flip()

        running = True
        while running: 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    running = False
