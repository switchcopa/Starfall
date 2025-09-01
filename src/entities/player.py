import pygame
from src.core.config import WINDOW_WIDTH, WINDOW_HEIGHT
from src.entities.laser import Laser
from time import time 

pygame.init()
player_image_path = "C:/Users/100TR/Starfall/assets/images/player.png"
stronger_player_image_path = "C:/Users/100TR/Starfall/assets/images/stronger_player.png"

player_image = pygame.image.load(player_image_path)
player_image = pygame.transform.scale(player_image, (100, 100)) 

stronger_player_image = pygame.image.load(player_image_path) 
stronger_player_image = pygame.transform.scale(stronger_player_image, (100,100))

class Player: 
    def __init__(self, health, speed, image): 
        self.x = WINDOW_WIDTH // 2 - 60 
        self.y = WINDOW_HEIGHT - 200
        self.health = health 
        self.speed = speed
        self.img = image 
        self.rect = self.img.get_rect()
        self.last_shot = time()

    def display(self, screen): 
        self.rect.x = self.x 
        self.rect.y = self.y 

        screen.blit(self.img, self.rect)

    def display_hitbox(self, screen): 
        hitbox = self.rect.inflate(-30, -30)

        line_thickness = 2
        pygame.draw.rect(screen, (255, 0, 0), hitbox, line_thickness)

    def move(self): 
        keys = pygame.key.get_pressed() 

        if keys[pygame.K_LEFT] and self.x > 0: 
            self.x -= self.speed 
        if keys[pygame.K_RIGHT] and self.x < WINDOW_WIDTH - self.img.get_width(): 
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > 0: 
            self.y -= self.speed 
        if keys[pygame.K_DOWN] and self.y < WINDOW_HEIGHT - self.img.get_width(): 
            self.y += self.speed 
