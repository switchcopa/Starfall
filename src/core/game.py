import pygame 

BLACK = (0,0,0)
background_color = BLACK 
WIDTH = 900
HEIGHT = 600
caption = 'Starfall'
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption(caption)
screen.fill(background_color)
pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
