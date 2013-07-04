import os

import pygame
    

def draw_text(string, size, destiny, position):
    font = pygame.font.SysFont('Arial', size)
    text = font.render(string, True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.x = position[0]
    textRect.y = position[1]
    destiny.blit(text, textRect)

