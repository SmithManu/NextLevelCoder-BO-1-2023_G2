from dino_runner.utils.constants import SCREEN_WIDTH
from pygame.sprite import Sprite
class Obstacle(Sprite):

    def __init__(self, image_list, type):
        self.image_list = image_list
        self.image = image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.dead = False

    def update(self, game_speed):
        self.rect.x -= game_speed
        if self.rect.x <= -self.image.get_width():
            self.dead = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)
