import pygame 
import config

BLACK = (0,0,0)
background_color = BLACK 
caption = 'Starfall'
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))

pygame.display.set_caption(caption)
screen.fill(background_color)
pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
