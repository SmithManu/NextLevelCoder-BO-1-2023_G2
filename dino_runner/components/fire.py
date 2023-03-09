import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import FIRE, SCREEN_WIDTH


class Fire(Sprite):
    def __init__(self,player):
        self.image = pygame.transform.scale(FIRE, (40, 30))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y=player.dino_rect.y
        self.in_action=False

    def update(self, player ):
        self.rect.x += 30 

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
        