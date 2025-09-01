import pygame 

pygame.init()

sprite_sheet_path = "C:/Users/100TR/Starfall/assets/images/explosion.png" 
sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()

frames = []
frame_count = 20
frame_width = sprite_sheet.get_width() // frame_count
frame_height = sprite_sheet.get_height()

for i in range(frame_count):
    frame = sprite_sheet.subsurface(pygame.Rect(i*frame_width, 0, frame_width, frame_height))
    frames.append(frame)

class Explosion(pygame.sprite.Sprite): 
    def __init__(self, x, y): 
        self.frames = frames
        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.frame_delay = 3  
        self.counter = 0

    def update(self):
        self.counter += 1
        if self.counter >= self.frame_delay:
            self.counter = 0
            self.index += 1
            if self.index < len(self.frames):
                self.image = self.frames[self.index]
            else:
                self.kill()  
