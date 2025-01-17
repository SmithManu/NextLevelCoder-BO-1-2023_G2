from dino_runner.components.Obstacles.obstacle import Obstacle
import random

class Cactus(Obstacle):

    def __init__(self, image_list, posY):
        self.type = random.randint(0,2)
        super().__init__(image_list,self.type)
        self.rect.y = posY

    def draw(self, screen):
        super().draw(screen)
        if self.dead:
            self.image = self.image_list[3]#imagen cactus muerto
            self.rect.y = 380