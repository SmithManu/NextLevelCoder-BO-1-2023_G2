import pygame
from pygame.sprite import Sprite
from dino_runner.components.Obstacles.obstacle import Obstacle
from dino_runner.components.Obstacles.powerUp import PowerUp
from dino_runner.components.fire import Fire
from dino_runner.utils.constants import COLORS2, HEART, RUNNING, DUCKING, JUMPING, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD

class Dinosaur(Sprite):
    POS_X = 80
    POS_Y = 310
    POS_BIG_Y=110
    POS_Y_DUCKING = 350
    JUMP_VEL = 8.5

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.POS_X
        self.dino_rect.y = self.POS_Y
        self.step_index = 0
        self.dino_state = [True, False, False]
        self.jump_vel = self.JUMP_VEL
        self.points = 0
        self.life = 3
        self.name = ""
        self.power_up=[False, False, False]
        self.fires = []
        self.power_up_time = [500,500,500]

        self.otro=self.image.get_width()
        self.otro2=self.image.get_height()
        self.rect_otro = (pygame.transform.scale(self.image, (280,SCREEN_HEIGHT))).get_rect()

    def update(self, user_input):
        self.temporizadorAtributo() 
        for fire in self.fires:
            fire.update(self)
        if self.dino_state[0]:
            self.run()
        elif self.dino_state[1] and not self.power_up[2]:
            self.duck()
        elif self.dino_state[2]:
            self.jump()
        #CONTROL DE ESTADOS
        if user_input[pygame.K_DOWN] and not self.dino_state[2]:
            self.dino_state = [False, True, False]
        elif user_input[pygame.K_UP] and not self.dino_state[1]:
            self.dino_state = [False, False, True]
        elif not self.dino_state[2]:
            self.dino_state = [True, False, False]
        
        if self.step_index >= 10 and user_input[pygame.K_SPACE] and self.power_up[1]:
            self.fires.append(Fire(self))

        self.step_index = (self.step_index + 1) % 11

    def draw(self, screen):
        for number in range(self.life):
            screen.blit(HEART, ( 50+30*number, SCREEN_HEIGHT-60))

        for fire in self.fires:
            fire.draw(screen)
        
        if(self.power_up[2]):
            if(self.otro<280):
                self.otro+=2
                self.otro2+=2
                self.dino_rect.y-=2
            big_dino = pygame.transform.scale(self.image, (self.otro, self.otro2))
            screen.blit(big_dino, (self.dino_rect.x, self.dino_rect.y))
        else:
            screen.blit(self.image, self.dino_rect)
        
        if self.power_up[0]:
            shield = pygame.transform.scale(SHIELD, (140, 140))
            screen.blit(shield, (self.dino_rect.x - 30, self.dino_rect.y - 30))

        for index in range(len(self.power_up)):
            if self.power_up[index]:
                self.draw_barra(index, screen)

        
    def draw_barra(self, index, screen):
        power_up_width = self.power_up_time[index] 
        power_up_x = SCREEN_WIDTH - power_up_width-20
        power_up_y = SCREEN_HEIGHT - 20*(index+2) # o cualquier otra posición vertical que desees
        pygame.draw.rect(screen, COLORS2[index], (power_up_x, power_up_y, power_up_width, 20))

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        Y = self.POS_Y + self.image.get_height()-self.otro2
        self.modificPos(self.POS_X, self.POS_Y if not self.power_up[2] else Y)

    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.modificPos(self.POS_X,self.POS_Y_DUCKING if not self.power_up[2] else self.POS_BIG_Y)

    def jump(self):
        self.image = JUMPING
        if self.dino_state[2]:
            self.dino_rect.y -= self.jump_vel*4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.POS_Y if not self.power_up[2] else self.POS_BIG_Y
            self.dino_state[2] = False
            self.jump_vel = self.JUMP_VEL
    
    def check_pos_misil(self):
        if(len(self.fires)!=0):
            for fire in self.fires:    
                if fire.rect.x > SCREEN_WIDTH:
                    self.fires.remove(fire)
    
    def modificPos(self, x, y): #Agregue una funcion para modificar posicion
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = x
        self.dino_rect.y = y

    def check_collision(self, object):
        rect = self.dino_rect if not self.power_up[2] else self.rect_otro
        if rect.colliderect(object.rect):
            if isinstance(object, Obstacle) and not object.dead:
                object.dead=True
                if not self.power_up[0] and not self.power_up[2]:
                    self.life-=1
            elif  isinstance(object, PowerUp):
                object.darPowerUp(self)
    
    def check_colicion_fires(self, obstacle):
        if(len(self.fires)!=0):
            for fire in self.fires:
                if fire.rect.colliderect(obstacle.rect): 
                    self.fires.remove(fire)
                    obstacle.dead=True

    def temporizadorAtributo(self):
        for index in range(len(self.power_up)):
            if(self.power_up[index]):
                self.control(index)
            elif(index == 2):
                self.otro=self.image.get_width()
                self.otro2=self.image.get_height()
        
    def control(self, index):
        self.power_up_time[index]-=1
        if(self.power_up_time[index]<=0):
            self.power_up_time[index]=500
            self.power_up[index]=False