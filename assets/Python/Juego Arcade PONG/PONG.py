import pygame
import random

# Inicializar pygame
pygame.init()

# Configuraciones de la pantalla
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 50
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configuraciones del juego
FPS = 60
SPEED = 5
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Crear la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Función para dibujar las paletas
def draw_paddle(paddle):
    pygame.draw.rect(screen, WHITE, paddle)

# Función para dibujar la pelota
def draw_ball(ball):
    ball_center = (ball.x + ball.width // 2, ball.y + ball.height // 2)
    ball_radius = min(ball.width // 2, ball.height // 2)
    pygame.draw.circle(screen, WHITE, ball_center, ball_radius)

# Función para dibujar el botón de reinicio
def draw_button():
    button_rect = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 - BUTTON_HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(screen, WHITE, button_rect)
    font = pygame.font.Font(None, 36)
    text = font.render("Restart", True, BLACK)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)
    return button_rect

# Función para mover la pelota
def move_ball(ball, ball_speed):
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]
    return ball

# Función para rebotar la pelota en las paredes superior e inferior
def check_wall_collision(ball, ball_speed):
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] *= -1
    return ball, ball_speed

# Función para rebotar la pelota en las paletas
def check_paddle_collision(ball, paddle1, paddle2, ball_speed):
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed[0] *= -1
    return ball_speed

# Función principal del juego
def main():
    paddle1 = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
    ball_speed = [BALL_SPEED_X, BALL_SPEED_Y]
    button_rect = None
    game_over = False

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
                if button_rect.collidepoint(event.pos):
                    main()  # Reiniciar el juego

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paddle1.top > 0:
            paddle1.y -= SPEED
        if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
            paddle1.y += SPEED
        if keys[pygame.K_UP] and paddle2.top > 0:
            paddle2.y -= SPEED
        if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
            paddle2.y += SPEED

        screen.fill(BLACK)
        draw_paddle(paddle1)
        draw_paddle(paddle2)
        draw_ball(ball)

        ball = move_ball(ball, ball_speed)
        ball, ball_speed = check_wall_collision(ball, ball_speed)
        ball_speed = check_paddle_collision(ball, paddle1, paddle2, ball_speed)

        if ball.right < 0 or ball.left > WIDTH:
            game_over = True
            button_rect = draw_button()

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
