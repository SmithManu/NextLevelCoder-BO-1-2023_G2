import pygame
from dino_runner.utils.constants import COLORS, SCREEN_HEIGHT, SCREEN_WIDTH

class TextUtils:

    FONT_STYLE = "freesansbold.ttf"

    def get_score(self, points, color=COLORS["BLACK"]):
        font = pygame.font.Font(self.FONT_STYLE, 20)
        text = font.render("Points: "+str(points), True, color)
        text_rect = text.get_rect()
        text_rect.center = (1000, 40)
        return text,text_rect
    
    def get_centered_message(self, message, width = SCREEN_WIDTH//2, height = SCREEN_HEIGHT//2, color=COLORS["BLACK"], n = 30):
        font = pygame.font.Font(self.FONT_STYLE, n)
        text = font.render(message, True, color)
        text_rect = text.get_rect()
        text_rect.center = (width, height)
        return text,text_rect
