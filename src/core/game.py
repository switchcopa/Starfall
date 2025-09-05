import pygame 
from src.entities.player import Player, player_image_path, stronger_player_image_path, player_image, stronger_player_image
from time import time 
import random 
from src.entities.asteroid import Asteroid
from src.entities.laser import Laser
from src.core.config import WINDOW_HEIGHT, WINDOW_WIDTH
from src.ui.UI import UI

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
        # --- Initialization ---
        pygame.display.set_caption(self.caption)
        self.screen.fill(self.background_color)

        health = 100
        speed = 12
        player = Player(health, speed, image=stronger_player_image)
        asteroids = []
        lasers = []
        base_scrolling_y = 0
        last_spawn_check = time()
        clock = pygame.time.Clock()
        self.start_time = time()
        self.running_time = 0
        self.over = False

        # --- Load background ---
        background_image = pygame.image.load(
            "C:/Users/100TR/Starfall/assets/images/space_background.jpg"
        ).convert()
        background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

        # --- Initialize UI ---
        ui = UI(screen=self.screen, player=player, max_time=180)

        # --- Play background music ---
        background_music.play()

        # --- Main loop ---
        running = True
        while running:
            clock.tick(60)  # limit FPS
            curr_time = time()
            self.running_time = curr_time - self.start_time

            # --- Event handling ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()

            # --- Toggle pause ---
            if keys[pygame.K_p]:
                ui.paused = not ui.paused

            if ui.paused:
                # Draw pause overlay
                self.screen.blit(background_image, (0, base_scrolling_y - self.screen_height))
                self.screen.blit(background_image, (0, base_scrolling_y))
                ui.draw_overlay("PAUSED", "Press P to resume")
                pygame.display.flip()
                continue  # skip updates while paused

            # --- Scroll background ---
            base_scrolling_y += 0.5
            if base_scrolling_y >= self.screen_height:
                base_scrolling_y = 0

            # --- Difficulty / aggression ---
            if self.running_time <= 30:
                aggression, difficulty = 1, 1
            elif self.running_time <= 60:
                aggression, difficulty = 0.75, 2
            else:
                aggression, difficulty = 0.65, 3

            # --- Spawn asteroids ---
            if curr_time - last_spawn_check >= aggression:
                last_spawn_check = curr_time
                if random.random() < 0.5:
                    asteroids.append(Asteroid())

            # --- Player actions ---
            player.move()
            if keys[pygame.K_x]:
                if curr_time - player.last_shot >= 0.30:
                    lasers.append(Laser(speed=24, damage=25, x=player.x+12, y=player.y-20))
                    laser_sound.play()
                    player.last_shot = curr_time

            # --- Update lasers ---
            new_lasers = []
            for laser in lasers:
                laser.move()
                hit = False
                for asteroid in asteroids[:]:
                    if laser.rect.colliderect(asteroid.rect):
                        asteroid.health -= laser.damage
                        hit = True
                        if asteroid.health <= 0:
                            asteroids.remove(asteroid)
                if not hit:
                    new_lasers.append(laser)
            lasers = new_lasers

            # --- Update asteroids ---
            for asteroid in asteroids[:]:
                asteroid.move()
                if asteroid.check_collision(player):
                    player.health -= asteroid.health // 2
                    rock_break_sound.play()
                    asteroids.remove(asteroid)

            # --- Check Game Over ---
            if player.health <= 0:
                big_monkey_fart.play()
                background_music.stop()
                ui.over = True

            # --- Draw everything ---
            self.screen.blit(background_image, (0, base_scrolling_y - self.screen_height))
            self.screen.blit(background_image, (0, base_scrolling_y))

            for laser in lasers:
                laser.display(self.screen)
            for asteroid in asteroids:
                asteroid.display(self.screen)
            player.display(self.screen)

            # --- Draw HUD ---
            ui.draw_hud(running_time=self.running_time)

            # --- Draw Game Over overlay if needed ---
            if ui.over:
                ui.draw_overlay("GAME OVER", "Press ESC to quit")
                if keys[pygame.K_ESCAPE]:
                    running = False

            # --- Update display ---
            pygame.display.flip()

