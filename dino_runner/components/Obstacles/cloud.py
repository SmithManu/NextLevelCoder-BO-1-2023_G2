from dino_runner.utils.constants import SCREEN_WIDTH
import random

class Cloud:

    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        ran = random.randint(0,2)
        self.rect.y = 200 if ran == 0 else 250 if ran==1 else 150
        self.rect.x = SCREEN_WIDTH if ran == 0 else SCREEN_WIDTH+100 if ran==1 else SCREEN_WIDTH*2

    def update(self, game_speed):
        self.rect.x -= game_speed-5
        if self.rect.x <= -self.image.get_width():
            ran = random.randint(0,2)
            self.rect.y = 200 if ran == 0 else 250 if ran==1 else 150
            ran = random.randint(0,2)
            self.rect.x = SCREEN_WIDTH if ran == 0 else SCREEN_WIDTH+100 if ran==1 else SCREEN_WIDTH*2

    def draw(self, screen):
        screen.blit(self.image, self.rect)