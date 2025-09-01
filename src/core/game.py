import pygame 
from src.entities.player import Player, player_image_path, stronger_player_image_path, player_image, stronger_player_image
from time import time 
import random 
from src.entities.asteroid import Asteroid
from src.entities.laser import Laser
from src.core.config import WINDOW_HEIGHT, WINDOW_WIDTH

pygame.init()
pygame.mixer.init()

laser_sound = pygame.mixer.Sound("C:/Users/100TR/Starfall/assets/sounds/laser_sound.mp3")
rock_break_sound = pygame.mixer.Sound("C:/Users/100TR/Starfall/assets/sounds/rock_break.mp3")
background_music = pygame.mixer.Sound("C:/Users/100TR/Starfall/assets/sounds/battle_music.mp3")
vine_boom = pygame.mixer.Sound("C:/Users/100TR/Starfall/assets/sounds/vine_boom.mp3")
big_monkey_fart = pygame.mixer.Sound("C:/Users/100TR/Starfall/assets/sounds/big_monkey_fart.mp3")

class Game: 
    def __init__(self, background_color, caption, window_width, window_height): 
        self.background_color = background_color 
        self.caption = caption
        self.screen_width = window_width
        self.screen_height = window_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.over = False
        self.difficutly = 0
        self.start_time = time()
        self.running_time = 0

    def run(self): 
        background_music.play()
        pygame.display.set_caption(self.caption)
        self.screen.fill(self.background_color) 

        health = 100
        speed = 1.5
        player = Player(health, speed, image=stronger_player_image)
        running = True
        last_spawn_check = time() 
        asteroids = []
        lasers = []
        base_scrolling_y = 0 
        
        background_image = pygame.image.load("C:/Users/100TR/Starfall/assets/images/space_background.jpg").convert()
        background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT)) 

        while running: 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    running = False

            if self.over:
                continue
            
            base_scrolling_y += 0.5 
            if base_scrolling_y >= self.screen_height: 
                base_scrolling_y = 0

            self.screen.blit(background_image, (0, base_scrolling_y - self.screen_height))
            self.screen.blit(background_image, (0, base_scrolling_y)) 
            curr_time = time() 
            asteroid = None
            keys = pygame.key.get_pressed()
            
            self.running_time = time() - self.start_time 

            if self.running_time <= 30:
                aggression = 1 
                difficulty = 1
            elif 30 < self.running_time <= 60:
                aggression = 0.75
                difficulty = 2
            elif 60 < self.running_time <= 180: 
                aggression = 0.25 
                difficulty = 3
                vine_boom.play()

            if curr_time - last_spawn_check >= aggression: 
                last_spawn_check = curr_time 
                
                if random.random() < 0.5: 
                    asteroid = Asteroid()
                    asteroids.append(asteroid)

            player.move()

            if keys[pygame.K_x]:
                curr_shot = time()
                if (curr_shot - player.last_shot >= 0.30):
                    laser = Laser(speed=2, damage=50, x=player.x+12, y=player.y-20)
                    print("Shot laser!")
                    laser_sound.play()
                    lasers.append(laser)
                    player.last_shot = curr_shot
            
            for x in lasers: 
                x.display(self.screen)
                x.move()

                for y in asteroids: 
                    if x.rect.colliderect(y.rect): 
                        y.health -= x.damage
                        lasers.remove(x)

                        if y.health == 0: 
                            asteroids.remove(y)
                del x 

            player.display(self.screen) 
            
            if asteroids:
                for x in asteroids: 
                    x.display(self.screen)
                    x.move()
                    
                    if x.check_collision(player): 
                        player.health -= x.health // 2
                        rock_break_sound.play()
                        asteroids.remove(x)
                        del x
            
            if player.health <= 0:
                print("Game over!")
                big_monkey_fart.play()
                background_music.stop()
                self.over = True

            pygame.display.flip()
