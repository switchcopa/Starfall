import pygame 
from src.core.config import WIDTH, HEIGHT
from src.entities.player import Player
from src.entities.asteroid import Asteroid

BLACK = (0,0,0)
background_color = BLACK 
caption = 'Starfall'
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption(caption)
screen.fill(background_color)
pygame.display.flip()

running = True
player = Player()
asteroid_health = 50
asteroid_speed = 4
asteroid = Asteroid(asteroid_health, asteroid_speed)

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
    
    screen.fill((0,0,0))
    player.handle_input()
    player.display(screen)
    asteroid.display(screen)
    asteroid.move()
    asteroid.check_collision(player)
    pygame.display.flip()
