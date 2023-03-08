import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Crear la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))

# Crear fuente para el texto
fuente = pygame.font.Font(None, 36)

# Crear cuadro de texto
cuadro_texto = pygame.Rect(ANCHO/2 - 100, ALTO/2 - 25, 200, 50)
texto = ''
texto_ingresado = False

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if not texto_ingresado:
                texto = ''
                texto_ingresado = True
            if evento.key == pygame.K_BACKSPACE:
                texto = texto[:-1]
            else:
                texto += evento.unicode
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if cuadro_texto.collidepoint(evento.pos):
                texto_ingresado = True
            else:
                texto_ingresado = False

    # Dibujar la ventana
    ventana.fill(BLANCO)
    pygame.draw.rect(ventana, NEGRO, cuadro_texto, 2)
    texto_superficie = fuente.render(texto, True, NEGRO)
    ventana.blit(texto_superficie, (cuadro_texto.x + 5, cuadro_texto.y + 5))
    pygame.display.update()
