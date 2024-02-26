# ball.py
import pygame
from constants import BALL_SPEED, WHITE

class Ball(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, 15, 15)
        self.speed_x = BALL_SPEED
        self.speed_y = BALL_SPEED

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self)
