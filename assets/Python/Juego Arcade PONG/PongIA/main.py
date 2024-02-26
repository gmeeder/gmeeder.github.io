# main.py
import pygame
import sys
from constants import WIDTH, HEIGHT, WHITE, BLACK
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    scoreboard = Scoreboard(font)

    player_paddle = Paddle(50, HEIGHT // 2 - 50)
    ai_paddle = Paddle(WIDTH - 60, HEIGHT // 2 - 50)
    ball = Ball(WIDTH // 2 - 7, HEIGHT // 2 - 7)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_paddle.top > 0:
            player_paddle.move("up")
        if keys[pygame.K_DOWN] and player_paddle.bottom < HEIGHT:
            player_paddle.move("down")

        if ball.colliderect(player_paddle) or ball.colliderect(ai_paddle):
            ball.speed_x *= -1

        ball.move()
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball.speed_y *= -1

        if ball.left <= 0:
            scoreboard.ai_scores()
            ball = Ball(WIDTH // 2 - 7, HEIGHT // 2 - 7)
        elif ball.right >= WIDTH:
            scoreboard.player_scores()
            ball = Ball(WIDTH // 2 - 7, HEIGHT // 2 - 7)

        ai_paddle.y = ball.y

        screen.fill(BLACK)
        player_paddle.draw(screen)
        ai_paddle.draw(screen)
        ball.draw(screen)
        scoreboard.draw(screen, WIDTH)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
