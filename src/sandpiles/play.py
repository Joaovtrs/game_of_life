import numpy as np
import pygame
from pygame.locals import *


def draw(fps):
    screen.fill(black)

    for i, colum in enumerate(sandpiles):
        for j, cell in enumerate(colum):
            if cell == 1:
                skin = pygame.Surface((gride_size, gride_size))
                skin.fill(red)
                screen.blit(skin, (i * gride_size, j * gride_size))
            elif cell == 2:
                skin = pygame.Surface((gride_size, gride_size))
                skin.fill(green)
                screen.blit(skin, (i * gride_size, j * gride_size))
            elif cell == 3:
                skin = pygame.Surface((gride_size, gride_size))
                skin.fill(blue)
                screen.blit(skin, (i * gride_size, j * gride_size))
            elif cell > 3:
                skin = pygame.Surface((gride_size, gride_size))
                skin.fill(white)
                screen.blit(skin, (i * gride_size, j * gride_size))

    txt2 = font2.render(f"FPS: {fps:.2f}", True, white)
    txt2_rect = txt2.get_rect()
    txt2_rect.topleft = (10, 10)
    screen.blit(txt2, txt2_rect)


def next_generation():
    global sandpiles
    new_sandpiles = np.zeros(gride)

    for i in range(gride[0]):
        for j in range(gride[1]):
            new_sandpiles[i][j] = sandpiles[i][j]

    for i in range(gride[0]):
        for j in range(gride[1]):
            if sandpiles[i][j] >= 4:
                new_sandpiles[i][j] -= 4
                if i > 0:
                    new_sandpiles[i - 1][j] += 1
                if i < gride[0] - 1:
                    new_sandpiles[i + 1][j] += 1
                if j > 0:
                    new_sandpiles[i][j - 1] += 1
                if j < gride[1] - 1:
                    new_sandpiles[i][j + 1] += 1

    sandpiles = new_sandpiles


playing = True
clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Control variables
window_height = 500
window_length = 700
gride_size = 5
gride = (int(window_length / gride_size), int(window_height / gride_size))

pygame.init()
screen = pygame.display.set_mode((window_length, window_height))
pygame.display.set_caption('Name')

try:
    font = pygame.font.Font('RobotoMono-Bold.ttf', 100)
    font2 = pygame.font.Font('RobotoMono-Bold.ttf', 20)
except FileNotFoundError:
    font = pygame.font.Font(None, 100)
    font2 = pygame.font.Font(None, 20)

sandpiles = np.zeros(gride)
sandpiles[gride[0] // 2][gride[1] // 2] = 100000

paused = False

while playing:
    clock.tick(20)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False

        if event.type == KEYDOWN:
            if event.key == 32:
                paused = not paused

    if not paused:
        for _ in range(3):
            next_generation()
        draw(clock.get_fps())

        pygame.display.update()

pygame.quit()
exit()
