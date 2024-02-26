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

# Dimensiones del ladrillo
ANCHO_LADRILLO = 60
ALTO_LADRILLO = 20
NUM_LADRILLOS_FILA = 10
NUM_FILAS_LADRILLOS = 4
ESPACIO_ENTRE_LADRILLOS = 4

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

# Clase del ladrillo
class Ladrillo(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface([ANCHO_LADRILLO, ALTO_LADRILLO])
        self.image.fill(color)
        self.rect = self.image.get_rect()

# Función para reiniciar el juego
def reiniciar_juego():
    global paleta, bola
    todos_los_sprites.empty()
    ladrillos.empty()
    puntaje = 0

    # Crear los ladrillos
    for fila in range(NUM_FILAS_LADRILLOS):
        for columna in range(NUM_LADRILLOS_FILA):
            ladrillo = Ladrillo(ROJO)
            ladrillo.rect.x = columna * (ANCHO_LADRILLO + ESPACIO_ENTRE_LADRILLOS)
            ladrillo.rect.y = fila * (ALTO_LADRILLO + ESPACIO_ENTRE_LADRILLOS) + 30
            ladrillos.add(ladrillo)
            todos_los_sprites.add(ladrillo)

    # Crear los sprites
    paleta = Paleta()  # Mover esta línea arriba
    bola = Bola()
    todos_los_sprites.add(paleta)  # Mover esta línea arriba
    todos_los_sprites.add(bola)

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
pantalla = pygame.display.set_mode([ANCHO_PANTALLA, ALTO_PANTALLA])
pygame.display.set_caption('Breakout')

# Crear los sprites
todos_los_sprites = pygame.sprite.Group()
ladrillos = pygame.sprite.Group()

# Reiniciar el juego
reiniciar_juego()

puntaje = 0
fuente = pygame.font.Font(None, 36)

reloj = pygame.time.Clock()

# Botón de reinicio
boton_reinicio = pygame.Rect(10, 10, 100, 50)

# Bucle principal del juego
jugando = True
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if boton_reinicio.collidepoint(evento.pos):
                    reiniciar_juego()

    # Actualizar los sprites
    todos_los_sprites.update()

    # Verificar colisión entre la bola y la paleta
    if pygame.sprite.collide_rect(bola, paleta):
        bola.vel_y = -bola.vel_y

    # Verificar colisión entre la bola y los ladrillos
    ladrillos_destruidos = pygame.sprite.spritecollide(bola, ladrillos, True)
    for ladrillo in ladrillos_destruidos:
        bola.vel_y = -bola.vel_y
        puntaje += 1

    # Limpiar la pantalla
    pantalla.fill(NEGRO)

    # Dibujar los sprites
    todos_los_sprites.draw(pantalla)

    # Mostrar puntaje
    texto_puntaje = fuente.render("Puntaje: " + str(puntaje), True, BLANCO)
    pantalla.blit(texto_puntaje, (10, 10))

    # Dibujar botón de reinicio
    pygame.draw.rect(pantalla, BLANCO, boton_reinicio)
    texto_reinicio = fuente.render("Restart", True, NEGRO)
    pantalla.blit(texto_reinicio, (20, 20))

    # Actualizar la pantalla
    pygame.display.flip()

    # Establecer la velocidad del juego
    reloj.tick(60)

# Salir de Pygame
pygame.quit()
