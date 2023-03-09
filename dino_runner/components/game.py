import pygame
from dino_runner.components.text_utils import TextUtils
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, GAMEOVER, RESET, GAME, MUSIC_GAME, COLORS
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
        self.game_speed = 15
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur() #Creamos nuestro dinosaurio
        self.obstacles = ObstacleManager()
        self.state = "menu"
        self.text_utils = TextUtils()
        self.running = True
        self.day_state="morning"
        self.day_num = 255
        self.max_points = 0
        self.max_name = ""

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
                MUSIC_GAME[1].set_volume(0.1)
                self.update()
                self.draw()
            elif self.state == "game_over":
                MUSIC_GAME[1].stop()
                MUSIC_GAME[2].play()
                MUSIC_GAME[2].set_volume(0.1)
                self.game_over_draw()
            else:
                break
        pygame.quit()

    def update(self):
        user_input = pygame.key.get_pressed()
        self.obstacles.update(self)
        self.player.update(user_input) #Acualizamos objeto dinosaurio
        self.player.check_collision(self.obstacles.cactus)
        self.player.check_collision(self.obstacles.birds)
        self.player.check_collision(self.obstacles.powerUp)
        self.player.check_colicion_fires(self.obstacles.cactus)
        self.player.check_colicion_fires(self.obstacles.birds)
        if self.player.life <= 0:
            if self.player.points>self.max_points:
                self.max_points=self.player.points
                self.max_name = self.player.name
            self.day_num = 255
            self.game_speed = 15
            self.day_state = "morning"
            self.state = "game_over"
        
    def draw(self):
        self.clock.tick(FPS)
        self.day()
        if(self.player.points%100 == 0):
            self.game_speed += 1
        self.draw_background()
        self.score()
        self.obstacles.draw(self.screen)
        self.player.draw(self.screen) #Dibujamos el dinosaurio
        pygame.display.update()
        pygame.display.flip()

    def day(self):
        if(self.player.points%500 == 0):
            self.day_state = "morning" if self.day_state=="evening" else "evening"
        if(self.day_num>0 and self.day_state == "morning"):
            self.day_num -= 1
        elif(self.day_num<255 and self.day_state == "evening"):
            self.day_num += 1


    def draw_background(self):
        self.screen.fill((self.day_num, self.day_num, self.day_num))
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
            text, text_rect = self.text_utils.get_centered_message(self.max_name+" "+str(self.max_points),SCREEN_WIDTH/2, 100)
            if (self.max_points>0):self.screen.blit(text, text_rect)
            pygame.display.update() # Actualizar la pantalla


    def score(self):
        self.player.points += 1
        text, text_rect = self.text_utils.get_score(self.player.points) if self.day_state == "evening" else self.text_utils.get_score(self.player.points,COLORS["WHITE"])
        self.screen.blit(text, text_rect)
        names = "Dino "+self.player.name
        text, text_rect = self.text_utils.get_centered_message(names,(SCREEN_WIDTH/2),40,COLORS["BLACK"],20) if self.day_state == "evening" else self.text_utils.get_centered_message(names,(SCREEN_WIDTH/2),40,COLORS["WHITE"],20)
        self.screen.blit(text, text_rect)
