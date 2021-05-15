import pygame
from pygame.locals import *

funcionando = True
clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
gray = (20, 20, 20)

# Control variables
window_height = 300
window_length = 600
gride_size = 20

pygame.init()
screen = pygame.display.set_mode((window_length, window_height))
pygame.display.set_caption('Game of Life')

while funcionando:
    clock.tick(60)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == QUIT:
            funcionando = False

    for x in range(0, window_length, gride_size):
        pygame.draw.line(screen, gray, (x, 0), (x, window_height))
    for y in range(0, window_height, gride_size):
        pygame.draw.line(screen, gray, (0, y), (window_length, y))

    pygame.display.update()

pygame.quit()
exit()
