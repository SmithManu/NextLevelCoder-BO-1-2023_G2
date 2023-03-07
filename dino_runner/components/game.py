import pygame
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, GAMEOVER, RESET, GAME
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
            self.events()
            if self.state == "menu":
                self.menu_draw()
            elif self.state == "playing":
                self.update()
                self.draw()
            elif self.state == "game_over":
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

        # Dibujar los puntos del jugador
        font = pygame.font.SysFont("comicsansms", 25)
        puntos_texto = font.render(f"Score: {self.player.points}", True, (0, 0, 0))
        puntos_rect = puntos_texto.get_rect()
        puntos_rect.topright = (self.screen.get_width() - 50, 10)
        self.screen.blit(puntos_texto, puntos_rect)

        self.player.draw(self.screen) #Dibujamos el dinosaurio
        self.obstacles.draw(self.screen)
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
        # Obtener las dimensiones de la ventana
        ventana_ancho, ventana_alto = self.screen.get_size()

        # Redimensionar la imagen al tamaño de la ventana
        GAME_redimensionado = pygame.transform.scale(GAME, (ventana_ancho, ventana_alto))

        # Calcular la posición de la imagen redimensionada para que se centre en la ventana
        posX = (ventana_ancho - GAME_redimensionado.get_width()) // 2
        posY = (ventana_alto - GAME_redimensionado.get_height()) // 2

        # Dibujar la imagen redimensionada en la ventana en la posición calculada
        self.screen.blit(GAME_redimensionado, (posX, posY))

        # Actualizar la pantalla
        pygame.display.update()