from dino_runner.components.Obstacles.obstacle import Obstacle
import random

class Bird(Obstacle):

    def __init__(self, image_list):
        super().__init__(image_list, 0)
        self.step_index = 0
        self.rect.y = 200 if random.randint(0,1)==0 else 300 if random.randint(0,1)==0 else 250

    def update(self, game_speed):
        self.step_index += 1
        if self.step_index >= 10:
            self.step_index = 0
        self.image = self.image_list[0] if self.step_index < 5 else self.image_list[1]
        super().update(game_speed)