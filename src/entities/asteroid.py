import pygame 
from random import randint
from src.core.config import WINDOW_WIDTH, WINDOW_HEIGHT 

pygame.init() 
asteroid_image_path = "../../assets/images/small_asteroid.png"
bigger_asteroid_image_path = "../../assets/images/big_asteroid.png"

asteroid_image = pygame.image.load(asteroid_image_path) 
bigger_asteroid_image = pygame.image.load(bigger_asteroid_image_path) 

class Asteroid:
    def __init__(self, health, speed): 
        self.x = 30 * (-1) 
        self.y = randint(100, WINDOW_WIDTH - 100) 
        self.chance = randint(0, 1)
       
        if self.chance == 0:
            self.type = "small_asteroid"
            self.size_x = randint(70, 120)
            self.size_y = randint(70, 130)
            self.img = pygame.transform.scale(asteroid_image, (self.size_x, self.size_y))
        else:
            self.type = "big_asteroid"
            self.size_x = randint(120, 150)
            self.size_y = randint(130, 160) 
            self.img = pygame.transform.scale(bigger_asteroid_image, (self.size_x, self.size_y))

        self.rect = self.img.get_rect()
        self.hitbox = self.rect.inflate(-30, -30)

    def display(self, screen): 
        self.rect.x = self.x 
        self.rect.y = self.y

        screen.blit(self.img, self.rect)

    def display_hitbox(self, screen): 
        line_thickness = 2 
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, line_thickness)

    def move(self): 
        self.y += self.speed

    def check_collision(self, player): 
        if self.hitbox.colliderect(player.rect): 
            return True
        else: return False
