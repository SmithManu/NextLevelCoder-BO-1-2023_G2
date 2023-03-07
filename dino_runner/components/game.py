import pygame
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, GAMEOVER, RESET
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.Obstacles.obstacle_manager import ObstacleManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE) #Titulo
        pygame.display.set_icon(ICON) #Icono del juego
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur() #Creamos nuestro dinosaurio
        self.obstacles = ObstacleManager()
        self.state = "menu"

    def run(self):
        # Game loop: events - update - draw
        while True:
            if self.state == "menu":
                self.menu_events()
                self.menu_draw()
            elif self.state == "playing":
                self.events()
                self.update()
                self.draw()
            elif self.state == "game_over":
                self.game_over_events()
                self.game_over_draw()
            else:
                break
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = "exit"

    def update(self):
        user_input = pygame.key.get_pressed()
        self.obstacles.update(self)
        self.player.update(user_input) #Acualizamos objeto dinosaurio

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((163, 228, 215))
        self.draw_background()
        self.player.draw(self.screen) #Dibujamos el dinosaurio
        self.obstacles.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()
        if self.player.is_dead:
            self.state = "game_over"

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def game_over_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = "exit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.state = "menu"
                    self.player = Dinosaur() #Creamos nuestro dinosaurio
                    self.obstacles = ObstacleManager()

    def game_over_draw(self):
        posX = (SCREEN_WIDTH-GAMEOVER.get_width())/2
        posY = (SCREEN_HEIGHT-GAMEOVER.get_height())/2
        self.screen.blit(GAMEOVER, (posX, posY))
        posx = (SCREEN_WIDTH-RESET.get_width())/2
        posy = (SCREEN_HEIGHT+RESET.get_height())/2
        self.screen.blit(RESET, (posx, posy))
        pygame.display.update()


    def menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = "exit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.state = "playing"

    def menu_draw(self):
        self.screen.fill((163, 228, 215))
        font = pygame.font.Font(None, 30)
        text = font.render("Press ENTER to play", True, (0, 0, 0))
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        self.screen.blit(text, text_rect)
        pygame.display.update()