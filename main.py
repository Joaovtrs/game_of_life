import pygame
import numpy as np
from pygame.locals import *


def draw():
    screen.fill(black)

    for i, colum in enumerate(lifes):
        for j, cell in enumerate(colum):
            if cell:
                screen.blit(skin, (i * gride_size, j * gride_size))

    for x in range(0, window_length, gride_size):
        pygame.draw.line(screen, gray, (x, 0), (x, window_height))
    for y in range(0, window_height, gride_size):
        pygame.draw.line(screen, gray, (0, y), (window_length, y))


funcionando = True
clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (50, 50, 50)

# Control variables
window_height = 500
window_length = 700
gride_size = 20
gride = (int(window_length / gride_size), int(window_height / gride_size))
lifes = np.random.randint(2, size=gride)
skin = pygame.Surface((gride_size, gride_size))
skin.fill(white)

pygame.init()
screen = pygame.display.set_mode((window_length, window_height))
pygame.display.set_caption('Game of Life')

while funcionando:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            funcionando = False
        
        if event.type == KEYDOWN:
            if event.key == 32:
                lifes = np.random.randint(2, size=gride)

    draw()

    pygame.display.update()

pygame.quit()
exit()
