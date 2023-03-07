import pygame
import random
from dino_runner.components.Obstacles.cactus import Cactus
from dino_runner.components.Obstacles.bird import Bird
from dino_runner.components.Obstacles.cloud import Cloud
from dino_runner.utils.constants import SMALL_CACTUS, BIRD, LARGE_CACTUS, CLOUD

class ObstacleManager:
    def __init__(self):
        self.obstacle = Cactus(SMALL_CACTUS, 325)
        self.clouds = [Cloud(CLOUD),Cloud(CLOUD),Cloud(CLOUD)]
    def update(self, game):
        for cloud in self.clouds:
            cloud.update(game.game_speed)
        self.obstacle.update(game.game_speed)
        if game.player.dino_rect.colliderect(self.obstacle.rect):
                game.player.is_dead = True
        if self.obstacle.dead:
            ran = random.randint(0,2)
            self.obstacle = Cactus(SMALL_CACTUS, 325) if ran == 0 else Bird(BIRD) if ran==1 else Cactus(LARGE_CACTUS, 300)

    def draw(self, screen):
        self.obstacle.draw(screen)
        for cloud in self.clouds:
            cloud.draw(screen)

