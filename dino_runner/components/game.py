import pygame
from dino_runner.components.text_utils import TextUtils
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, GAMEOVER, RESET, GAME, MUSIC_GAME
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.Obstacles.obstacle_manager import ObstacleManager

class Game:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
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
        self.text_utils = TextUtils()
        self.running = True

    def run(self):
        # Game loop: events - update - draw
        while True:
            self.events()
            if self.state == "menu":
                MUSIC_GAME[2].stop()
                MUSIC_GAME[0].play(-1)
                self.menu_draw()
            elif self.state == "playing":
                MUSIC_GAME[0].stop()
                MUSIC_GAME[1].play(-1)
                self.update()
                self.draw()
            elif self.state == "game_over":
                MUSIC_GAME[1].stop()
                MUSIC_GAME[2].play()
                self.game_over_draw()
            else:
                break
        pygame.quit()

    def update(self):
        user_input = pygame.key.get_pressed()
        self.obstacles.update(self)
        self.player.update(user_input) #Acualizamos objeto dinosaurio

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.score()
        self.obstacles.draw(self.screen)
        self.player.draw(self.screen) #Dibujamos el dinosaurio
        pygame.display.update()
        pygame.display.flip()
        if self.player.is_dead:
            self.state = "game_over"

    def draw_background(self):
        self.screen.fill((255, 255, 255))
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def game_over_draw(self):
        posX = (SCREEN_WIDTH-GAMEOVER.get_width())/2
        posY = (SCREEN_HEIGHT-GAMEOVER.get_height())/2
        self.screen.blit(GAMEOVER, (posX, posY))
        posx = (SCREEN_WIDTH-RESET.get_width())/2
        posy = (SCREEN_HEIGHT+RESET.get_height())/2
        self.screen.blit(RESET, (posx, posy))
        pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = "exit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN  and self.state == "menu":
                    self.state = "playing"
                elif event.key == pygame.K_RETURN and self.state == "game_over":
                    self.state = "menu"
                    self.player = Dinosaur() #Creamos nuestro dinosaurio
                    self.obstacles = ObstacleManager()

    def menu_draw(self):
        # Redimensionar la imagen al tamaño de la ventana
        GAME_redimensionado = pygame.transform.scale(GAME, (SCREEN_WIDTH, SCREEN_HEIGHT))
        posX = (SCREEN_WIDTH - GAME_redimensionado.get_width()) // 2
        posY = (SCREEN_HEIGHT - GAME_redimensionado.get_height()) // 2
        name = "" # Nombre inicial vacío
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = "exit"
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.unicode.isalpha() and len(name) < 10: # Solo letras y un máximo de 10 caracteres
                        name += event.unicode
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1] # Borrar el último caracter
                    elif event.key == pygame.K_RETURN:
                        self.player.name = name # Guardar el nombre en el objeto player
                        self.state = "playing" # Cambiar de estado a "playing"
                        return
            self.screen.blit(GAME_redimensionado, (posX, posY))
            text, text_rect = self.text_utils.get_centered_message(f"NAME: {name}")
            self.screen.blit(text, text_rect)
            pygame.display.update() # Actualizar la pantalla


    def score(self):
        self.player.points += 1
        text, text_rect = self.text_utils.get_score(self.player.points)
        self.screen.blit(text, text_rect)
