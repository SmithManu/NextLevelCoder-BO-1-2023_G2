import pygame
import os

# Global Constants
pygame.mixer.init()
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SquashedCactus.png"))
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SquashedCactus.png"))
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))
FIRE = pygame.image.load(os.path.join(IMG_DIR, 'Other/Fire.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

GAME = pygame.image.load(os.path.join(IMG_DIR, 'Other/GAME.png'))
GAMEOVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png')) #Cargamos imagen gameover
RESET = pygame.image.load(os.path.join(IMG_DIR, 'Other/Reset.png')) #Cargamos imagen reset

DEFAULT_TYPE = "default"

COLORS = {
    "BLACK": (0,0,0),
    "WHITE": (255,255,255)
}

MUSIC_GAME = [
    pygame.mixer.Sound(os.path.join(IMG_DIR, 'Music/Game.mp3')),
    pygame.mixer.Sound(os.path.join(IMG_DIR, 'Music/Game1.mp3')),
    pygame.mixer.Sound(os.path.join(IMG_DIR, 'Music/Game2.mp3'))
]

POWER_UPS=[
    pygame.image.load(os.path.join(IMG_DIR, 'Other/PowerUpUp.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/PowerUpShield.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/PowerUpFire.png')),    
    pygame.image.load(os.path.join(IMG_DIR, 'Other/PowerUpBig.png'))
]