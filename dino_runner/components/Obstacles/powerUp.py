from random import randint
import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import POWER_UPS, SCREEN_WIDTH

class PowerUp(Sprite):
    def __init__(self):
        self.type =  randint (0, 3)
        if(self.type == 0):
            self.image = pygame.transform.scale(POWER_UPS[self.type], (100, 100))
        else:
            self.image = pygame.transform.scale(POWER_UPS[self.type], (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + randint (800, 1000)
        self.rect.y = randint (125, 185)

    def update (self, game_speed):
        self.rect.x -= game_speed-5

    def draw (self, screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))

    def darPowerUp (self, player):
        self.rect.x=-100 # mandarlo a crearse de nuevo
        if(self.type==0):
            player.life+=1
        elif(self.type==1 and not player.power_up[2]):
            player.power_up[0] =True
        elif(self.type==2 and not player.power_up[2]):
            player.power_up[1] =True
        elif(self.type==3 and not player.power_up[0] and not player.power_up[1]):
            player.power_up[2] =True
            

    
    
            
        
    
    