import pygame 
from player import Player, player_image_path, stronger_player_image_path

def handle_player(screen): 
    health = 100
    speed = 8
    player = Player(health, speed, player_image_path) 

    player.display(screen)
    player.display_hitbox(screen)
