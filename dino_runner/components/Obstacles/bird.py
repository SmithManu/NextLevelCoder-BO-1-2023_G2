from dino_runner.components.Obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SCREEN_WIDTH
import random

class Bird(Obstacle):

    def __init__(self, image_list):
        super().__init__(image_list, 0)
        self.step_index = 0
        posiY=[200,300,250]
        self.rect.y = posiY[random.randint(0,2)]
        self.rect.x=SCREEN_WIDTH+600

    def update(self, game_speed):
        self.step_index += 1
        if self.step_index >= 10:
            self.step_index = 0
        self.image = self.image_list[0] if self.step_index < 5 else self.image_list[1]
        if(not self.dead): #movimiento recto
            super().update(game_speed)
        else:
            if(self.rect.y<380): #movimiento en caida
                self.rect.y += 10 
                self.rect.x -= 30
            else:
                self.rect.x=-100    