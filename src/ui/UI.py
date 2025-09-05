
import pygame

class UI:
    def __init__(self, screen, player, max_time=180):
        self.screen = screen
        self.player = player
        self.max_time = max_time
        self.font = pygame.font.SysFont("Arial", 20, bold=True)
        self.big_font = pygame.font.SysFont("Arial", 50, bold=True)
        self.paused = False
        self.over = False

    def draw_health_bar(self):
        bar_width, bar_height = 200, 20
        health_ratio = max(self.player.health / 100, 0)
        pygame.draw.rect(self.screen, (255,0,0), (10, 10, bar_width, bar_height))
        pygame.draw.rect(self.screen, (0,255,0), (10, 10, bar_width * health_ratio, bar_height))
        health_text = self.font.render(f"Health: {self.player.health}", True, (255,255,255))
        self.screen.blit(health_text, (220, 10))

    def draw_time_bar(self, running_time):
        bar_width, bar_height = 200, 20
        time_ratio = min(running_time / self.max_time, 1)
        pygame.draw.rect(self.screen, (50,50,50), (10, 40, bar_width, bar_height))
        pygame.draw.rect(self.screen, (0,0,255), (10, 40, bar_width * time_ratio, bar_height))
        time_text = self.font.render(f"Time: {int(running_time)}s", True, (255,255,255))
        self.screen.blit(time_text, (220, 40))

    def draw_hud(self, running_time):
        self.draw_health_bar()
        self.draw_time_bar(running_time)

    def draw_overlay(self, title, subtitle=""):
        overlay = pygame.Surface(self.screen.get_size())
        overlay.set_alpha(180)
        overlay.fill((0,0,0))
        self.screen.blit(overlay, (0,0))

        title_text = self.big_font.render(title, True, (255,0,0))
        self.screen.blit(
            title_text,
            (self.screen.get_width()//2 - title_text.get_width()//2,
             self.screen.get_height()//2 - 50)
        )

        if subtitle:
            subtitle_text = self.font.render(subtitle, True, (255,255,255))
            self.screen.blit(
                subtitle_text,
                (self.screen.get_width()//2 - subtitle_text.get_width()//2,
                 self.screen.get_height()//2 + 10)
            )

