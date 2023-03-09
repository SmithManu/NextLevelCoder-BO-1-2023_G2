import random
from dino_runner.components.Obstacles.cactus import Cactus
from dino_runner.components.Obstacles.bird import Bird
from dino_runner.components.Obstacles.cloud import Cloud
from dino_runner.components.Obstacles.powerUp import PowerUp
from dino_runner.utils.constants import SCREEN_WIDTH, SMALL_CACTUS, BIRD, LARGE_CACTUS, CLOUD

class ObstacleManager:
    def __init__(self):
        self.clouds = [Cloud(CLOUD),Cloud(CLOUD),Cloud(CLOUD)]
        self.cactus = Cactus(SMALL_CACTUS, 325)
        self.birds=Bird (BIRD)
        self.powerUp=PowerUp()
        self.step_index_Birds=random.randint(0,250)
        self.step_index_powerUps=random.randint(0,250)

    def update(self, game):
        for cloud in self.clouds:
            cloud.update(game.game_speed)
        self.cactus.update(game.game_speed)
        self.birds.update(game.game_speed)
        self.powerUp.update(game.game_speed)
        self.crearCactus()
        self.crearBirds()
        self.crearPowerUp()

    def draw(self, screen):
        self.cactus.draw(screen)
        self.birds.draw(screen)
        self.powerUp.draw(screen)
        for cloud in self.clouds:
            cloud.draw(screen)

    def crearCactus(self):
        if self.cactus.rect.x < -self.cactus.rect.width:
            object = [Cactus(SMALL_CACTUS, 325),Cactus(LARGE_CACTUS, 300)]
            self.cactus = object[random.randint(0,1)]

    def crearBirds(self):
        if (self.cactus.rect.x <SCREEN_WIDTH //2)and self.birds.dead: #evita sobreponer
            print("cactus al medio")
            if self.step_index_Birds > 250 : #verifica que no haya pajaros
                self.birds=Bird (BIRD)
                self.step_index_Birds=random.randint(0,250)
            self.step_index_Birds+=1
    
    def crearPowerUp(self):
        if self.step_index_powerUps > 250 and self.powerUp.rect.x < -self.powerUp.rect.width:
            self.powerUp = PowerUp()
            self.step_index_powerUps=random.randint(0,250)
        self.step_index_powerUps+=1
