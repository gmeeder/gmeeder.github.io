import pygame
import random

# Definir algunos colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Tamaño de la pantalla
ANCHO_PANTALLA = 600
ALTO_PANTALLA = 400

# Dimensiones de la paleta
ANCHO_PALETA = 100
ALTO_PALETA = 10

# Dimensiones de la bola
DIAMETRO_BOLA = 20

# Velocidad inicial de la bola
VEL_BOLA_X = 5
VEL_BOLA_Y = -5

# Clase de la paleta
class Paleta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([ANCHO_PALETA, ALTO_PALETA])
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.x = (ANCHO_PANTALLA - ANCHO_PALETA) // 2
        self.rect.y = ALTO_PANTALLA - ALTO_PALETA - 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > ANCHO_PANTALLA - ANCHO_PALETA:
            self.rect.x = ANCHO_PANTALLA - ANCHO_PALETA

# Clase de la bola
class Bola(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([DIAMETRO_BOLA, DIAMETRO_BOLA])
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.x = (ANCHO_PANTALLA - DIAMETRO_BOLA) // 2
        self.rect.y = ALTO_PANTALLA - ALTO_PALETA - DIAMETRO_BOLA - 10
        self.vel_x = VEL_BOLA_X
        self.vel_y = VEL_BOLA_Y

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.rect.x <= 0 or self.rect.x >= ANCHO_PANTALLA - DIAMETRO_BOLA:
            self.vel_x = -self.vel_x
        if self.rect.y <= 0:
            self.vel_y = -self.vel_y

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
pantalla = pygame.display.set_mode([ANCHO_PANTALLA, ALTO_PANTALLA])
pygame.display.set_caption('Breakout')

# Crear los sprites
todos_los_sprites = pygame.sprite.Group()
paleta = Paleta()
bola = Bola()
todos_los_sprites.add(paleta)
todos_los_sprites.add(bola)

reloj = pygame.time.Clock()

# Bucle principal del juego
jugando = True
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # Actualizar los sprites
    todos_los_sprites.update()

    # Verificar colisión entre la bola y la paleta
    if pygame.sprite.collide_rect(bola, paleta):
        bola.vel_y = -bola.vel_y

    # Limpiar la pantalla
    pantalla.fill(NEGRO)

    # Dibujar los sprites
    todos_los_sprites.draw(pantalla)

    # Actualizar la pantalla
    pygame.display.flip()

    # Establecer la velocidad del juego
    reloj.tick(60)

# Salir de Pygame
pygame.quit()
