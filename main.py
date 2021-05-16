import numpy as np
import pygame
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
            neighbours = count_neighbours(i, j)

            if generation[i][j]:
                if neighbours >= 2 and neighbours <= 3:
                    new_generation[i][j] = 1
            else:
                if neighbours == 3:
                    new_generation[i][j] = 1

    generation = new_generation


def get_neighbours(x, y):
    global gride
    neighbours = []
    neighbours.append((
        (x - 1) % gride[0],
        (y - 1) % gride[1]
    ))
    neighbours.append((
        (x - 1) % gride[0],
        (y) % gride[1]
    ))
    neighbours.append((
        (x) % gride[0],
        (y - 1) % gride[1]
    ))
    neighbours.append((
        (x + 1) % gride[0],
        (y + 1) % gride[1]
    ))
    neighbours.append((
        (x + 1) % gride[0],
        (y) % gride[1]
    ))
    neighbours.append((
        (x) % gride[0],
        (y + 1) % gride[1]
    ))
    neighbours.append((
        (x + 1) % gride[0],
        (y - 1) % gride[1]
    ))
    neighbours.append((
        (x - 1) % gride[0],
        (y + 1) % gride[1]
    ))
    return neighbours


def count_neighbours(x, y):
    global generation
    return sum(generation[x_i][y_i] for x_i, y_i in get_neighbours(x, y))


def add_cell(abs_x, abs_y):
    global gride_size, generation
    x = abs_x // gride_size
    y = abs_y // gride_size
    generation[x][y] = 0 if generation[x][y] else 1


playing = True
clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (20, 20, 20)

# Control variables
tick = 60
window_height = 500
window_length = 700
gride_size = 20
gride = (int(window_length / gride_size), int(window_height / gride_size))
generation = np.random.randint(2, size=gride)
skin = pygame.Surface((gride_size, gride_size))
skin.fill(white)
paused = False

pygame.init()
screen = pygame.display.set_mode((window_length, window_height))
pygame.display.set_caption('Game of Life')

while playing:
    clock.tick(tick)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False

        if event.type == pygame.MOUSEBUTTONUP:
            add_cell(*pygame.mouse.get_pos())

        if event.type == KEYDOWN:
            if event.key == 32:
                generation = np.random.randint(2, size=gride)

            if event.key == 112:
                paused = not paused

            if event.key == 99:
                generation = np.zeros(gride)

    draw()
    if not paused:
        next_generation()

    pygame.display.update()

pygame.quit()
exit()
