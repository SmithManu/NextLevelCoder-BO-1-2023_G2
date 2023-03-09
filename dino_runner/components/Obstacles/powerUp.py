from random import randint
import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import POWER_UPS, SCREEN_WIDTH

class PowerUp(Sprite):
    def __init__(self):
        self.type =  randint (0, 3)
        if(self.type == 0):
            self.image = pygame.transform.scale(POWER_UPS[self.type], (55, 55))
        else:
            self.image = pygame.transform.scale(POWER_UPS[self.type], (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + randint (800, 1000)
        self.rect.y = randint (125, 185)

    def update (self, game_speed):
        self.rect.x -= game_speed

    def draw (self, screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))

    def darPowerUp (self, player):
        self.rect.x=-100 # mandarlo a crearse de nuevo
        if(self.type==0):
            player.life+=1
        elif(self.type==1):
            player.durationPowerUp=0
            player.power_up_shild =True
        elif(self.type==2):
            player.durationPowerUp_Fire=0
            player.power_up_fire =True
        elif(self.type==3):
            player.durationPowerUp_Big=0
            player.power_up_Big =True
            

    
    
            
        
    
    