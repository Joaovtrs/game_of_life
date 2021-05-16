import pygame
import numpy as np
from pygame.locals import *


def draw():
    screen.fill(black)

    for i, colum in enumerate(generation):
        for j, cell in enumerate(colum):
            if cell:
                screen.blit(skin, (i * gride_size, j * gride_size))

    for x in range(0, window_length, gride_size):
        pygame.draw.line(screen, gray, (x, 0), (x, window_height))
    for y in range(0, window_height, gride_size):
        pygame.draw.line(screen, gray, (0, y), (window_length, y))


def next_generation():
    global generation, gride
    new_generation = np.zeros(gride)

    for i in range(gride[0]):
        for j in range(gride[1]):
            new_generation[i][j] = generation[i][j]

    generation = new_generation


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
generation = np.random.randint(2, size=gride)
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
                generation = np.random.randint(2, size=gride)

    draw()
    next_generation()

    pygame.display.update()

pygame.quit()
exit()
