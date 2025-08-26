import pygame 
from src.entities.player import Player, player_image_path, stronger_player_image_path

pygame.init()

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
    
        health = 100
        speed = 8
        player = Player(health, speed, img_path=player_image_path)
        running = True
        while running: 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    running = False
            
            player.display(self.screen) 
            player.display_hitbox(self.screen)
            self.screen.fill(self.background_color)
