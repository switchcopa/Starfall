import pygame
from src.core.config import WINDOW_WIDTH, WINDOW_HEIGHT

pygame.init()
player_image_path = "C:/Users/100TR/Starfall/assets/images/player.png"
stronger_player_image_path = "../../assets/images/stronger_player.png"

class Player: 
    def __init__(self, health, speed, img_path): 
        self.x = WINDOW_WIDTH // 2  
        self.y = WINDOW_HEIGHT  // 2
        self.health = health 
        self.speed = speed
        self.img = pygame.image.load(img_path).convert_alpha()
        self.rect = self.img.get_rect()

    def display(self, screen): 
        self.rect.x = self.x 
        self.rect.y = self.y 

        screen.blit(self.img, self.rect)

    def display_hitbox(self, screen): 
        hitbox = self.rect.inflate(-30, -30)

        line_thickness = 2
        pygame.draw.rect(screen, (255, 0, 0), hitbox, line_thickness)
