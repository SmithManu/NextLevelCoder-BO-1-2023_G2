import pygame
from pygame.sprite import Sprite
from dino_runner.components.Obstacles.obstacle import Obstacle
from dino_runner.components.Obstacles.powerUp import PowerUp
from dino_runner.components.fire import Fire
from dino_runner.utils.constants import HEART, RUNNING, DUCKING, JUMPING, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD

class Dinosaur(Sprite):
    POS_X = 80
    POS_Y = 310
    POS_Y_DUCKING = 350
    JUMP_VEL = 8.5

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.POS_X
        self.dino_rect.y = self.POS_Y
        self.step_index = 0
        self.dino_running = True
        self.dino_ducking = False
        self.dino_jumping = False
        self.jump_vel = self.JUMP_VEL
        self.points = 0
        self.is_dead = False
        self.life = 3
        self.name = ""
        self.power_up=[False, False, False]
        self.fires = []
        self.jump_velocity = self.JUMP_VEL
        self.step_index_Fire = 0
        self.power_up_time = [500,500,500]

        self.otro=self.image.get_width()
        self.otro2=self.image.get_height()

    def update(self, user_input):
        self.is_dead = True if self.life == 0 else False
        self.temporizadorAtributo() 
        if(len(self.fires)!=0): #movimiento del fuego
            for fire in self.fires:
                fire.update(self)
        if self.dino_running:
            self.run()
        elif self.dino_ducking:
            self.duck()
        elif self.dino_jumping:
            self.jump()
        if user_input[pygame.K_DOWN] and not self.dino_jumping:
            self.modific(False, True, False)
        elif user_input[pygame.K_UP] and not self.dino_ducking:
            self.modific(False, False, True)
        elif not self.dino_jumping:
            self.modific(True, False, False)
        self.step_index += 1
        if self.step_index >= 10:
            self.step_index = 0
        if user_input[pygame.K_a] and self.power_up[1] and self.step_index_Fire>10:
            self.shoot()
            self.step_index_Fire=0
        self.step_index_Fire+=1

    def draw(self, screen):
        for number in range(self.life):
            screen.blit(HEART, ( 50+30*number, SCREEN_HEIGHT-60))
        
        if(self.power_up[2]):
            if(self.otro<280):
                self.otro+=2
                self.otro2+=2
            bigDino = pygame.transform.scale(self.image, (self.otro,self.otro2))
            big_y=self.dino_rect.y-200
            screen.blit(bigDino,(self.dino_rect.x, big_y))
        else:
            screen.blit(self.image, self.dino_rect)
            
        if(self.power_up[0]):
            sild = pygame.transform.scale(SHIELD, (140, 140))
            screen.blit(sild, (self.dino_rect.x-30, self.dino_rect.y-30))
        if(len(self.fires)!=0):
            for fire in self.fires:
                fire.draw(screen)
        if self.power_up[0]:
            self.draw_barra(0, screen)
        if self.power_up[1]:
            self.draw_barra(1, screen)
        if self.power_up[2]:
            self.draw_barra(2, screen)
        
    def draw_barra(self, index, screen):
        power_up_color = (0, 0, 0) # o cualquier otro color que desees
        power_up_width = self.power_up_time[index] 
        power_up_x = SCREEN_WIDTH - power_up_width-20
        power_up_y = SCREEN_HEIGHT - 20*(index+2) # o cualquier otra posición vertical que desees
        self.draw_power_up_timer(screen, power_up_color, power_up_x, power_up_y, power_up_width)

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.modificPos(self.POS_X,self.POS_Y)

    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.modificPos(self.POS_X,self.POS_Y_DUCKING)

    def jump(self):
        self.image = JUMPING
        if self.dino_jumping:
            self.dino_rect.y -= self.jump_vel*4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.POS_Y
            self.dino_jumping = False
            self.jump_vel = self.JUMP_VEL
    
    def shoot(self):
        self.fires.append(Fire(self))
    
    def check_pos_misil(self):
        if(len(self.fires)!=0):
            for fire in self.fires:    
                if fire.rect.x > SCREEN_WIDTH:
                    self.fires.remove(fire)

    def modific(self, running, ducking, jumping): #Agrege una funcion para modificar valores en uno
        self.dino_running = running
        self.dino_ducking = ducking
        self.dino_jumping = jumping 
    
    def modificPos(self, x, y): #Agregue una funcion para modificar posicion
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = x
        self.dino_rect.y = y

    def check_collision(self, object):
        if self.dino_rect.colliderect(object.rect):
            if isinstance(object, Obstacle) and not object.dead:
                object.dead=True
                if not self.power_up[2] and not self.power_up[0]:
                    self.life-=1
            elif  isinstance(object, PowerUp) and not self.power_up[2]:
                object.darPowerUp(self)
    
    def check_colicion_fires(self, obstacle):
        if(len(self.fires)!=0):
            for fire in self.fires:
                if fire.rect.colliderect(obstacle.rect): 
                    self.fires.remove(fire)
                    obstacle.dead=True
    
    def draw_power_up_timer(self, screen, color, x, y, width):
        pygame.draw.rect(screen, color, (x, y, width, 20))

    def temporizadorAtributo(self):
        if(self.power_up[0]):
            self.control(0)
        if(self.power_up[1]):
            self.control(1)
        if(self.power_up[2]):
            self.control(2)
        else:
            self.otro=self.image.get_width()
            self.otro2=self.image.get_height()
        
    def control(self, index):
        self.power_up_time[index]-=1
        if(self.power_up_time[index]<0):
            self.power_up_time[index]=500
            self.power_up[index]=False
        