import pygame
import random
from dino_runner.components.Obstacles.cactus import Cactus
from dino_runner.components.Obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, BIRD, LARGE_CACTUS

class ObstacleManager:
    def __init__(self):
        self.obstacle = Cactus(SMALL_CACTUS)

    def update(self, game):
        self.obstacle.update(game.game_speed)

        if game.player.dino_rect.colliderect(self.obstacle.rect):
                game.player.is_dead = True

        if self.obstacle.dead:
            ran = random.randint(0,2)
            self.obstacle = Cactus(SMALL_CACTUS) if ran == 0 else Bird(BIRD) if ran==1 else Cactus(LARGE_CACTUS)

    def draw(self, screen):
        self.obstacle.draw(screen)