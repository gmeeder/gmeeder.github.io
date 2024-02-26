# scoreboard.py
import pygame
from constants import WHITE

class Scoreboard:
    def __init__(self, font):
        self.player_score = 0
        self.ai_score = 0
        self.font = font

    def draw(self, screen, width):
        player_text = self.font.render("Player: " + str(self.player_score), True, WHITE)
        ai_text = self.font.render("AI: " + str(self.ai_score), True, WHITE)
        screen.blit(player_text, (20, 20))
        screen.blit(ai_text, (width - 120, 20))

    def player_scores(self):
        self.player_score += 1

    def ai_scores(self):
        self.ai_score += 1
