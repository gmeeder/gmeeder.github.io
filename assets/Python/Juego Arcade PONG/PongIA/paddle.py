# paddle.py
import pygame
from constants import PADDLE_SPEED, WHITE

class Paddle(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, 10, 100)

    def move(self, direction):
        if direction == "up":
            self.y -= PADDLE_SPEED
        elif direction == "down":
            self.y += PADDLE_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self)
