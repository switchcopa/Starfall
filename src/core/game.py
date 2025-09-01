import pygame 
from src.entities.player import Player, player_image_path, stronger_player_image_path, player_image, stronger_player_image
from time import time 
import random 
from src.entities.asteroid import Asteroid

pygame.init()

class Game: 
    def __init__(self, background_color, caption, window_width, window_height): 
        self.background_color = background_color 
        self.caption = caption
        self.screen_width = window_width
        self.screen_height = window_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.over = False
        
    def run(self): 
        pygame.display.set_caption(self.caption)
        self.screen.fill(self.background_color) 

        health = 100
        speed = 1
        player = Player(health, speed, image=stronger_player_image)
        running = True
        last_spawn_check = time() 
        asteroids = []

        while running: 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    running = False

            if self.over:
                continue
           
            curr_time = time() 
            asteroid = None

            if curr_time - last_spawn_check >= 1: 
                last_spawn_check = curr_time 
                if random.random() < 0.5: 
                    asteroid = Asteroid()
                    asteroids.append(asteroid)

            self.screen.fill(self.background_color)
            player.move()
            player.display(self.screen) 
            player.display_hitbox(self.screen)
            
            collided = False

            if asteroids:
                for x in asteroids: 
                    x.display(self.screen)
                    x.display_hitbox(self.screen)
                    
                    if x.check_collision(player): 
                        collided = True
                    x.move()
            
            if collided:
                self.over = True

            pygame.display.flip()
