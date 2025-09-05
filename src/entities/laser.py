import pygame 
from src.core.config import WINDOW_WIDTH, WINDOW_HEIGHT 

pygame.init()
laser_image_path = "C:/Users/100TR/Starfall/assets/images/laser.png"
laser_image = pygame.image.load(laser_image_path)
laser_image = pygame.transform.scale(laser_image, (20, 70))

class Laser: 
    def __init__(self, speed, damage, x, y): 
        self.x = x 
        self.y = y 
        self.speed = speed 
        self.damage = damage 
        self.img = laser_image
        self.rect = self.img.get_rect()

    def display(self, screen): 
        self.rect.x = self.x 
        self.rect.y = self.y 

        screen.blit(self.img, self.rect) 

    def display_hitbox(self, screen): 
        hitbox = self.rect.inflate(0, -20) 

        line_thickness = 2
        pygame.draw.rect(screen, (255, 0, 0), hitbox, line_thickness)

    def move(self): 
        self.y -= self.speed
