import random
import pygame
from pygame.locals import *


def random_point():
    global window_height, window_length
    return random.random() * window_length, random.random() * window_height


def dist_to_center(x, y):
    global window_height, window_length
    return ((window_length / 2 - x) ** 2 + (window_height / 2 - y) ** 2) ** 0.5


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
window_length = 500

pygame.init()
screen = pygame.display.set_mode((window_length, window_height))
pygame.display.set_caption('Name')

try:
    font = pygame.font.Font('RobotoMono-Bold.ttf', 100)
    font2 = pygame.font.Font('RobotoMono-Bold.ttf', 20)
except FileNotFoundError:
    font = pygame.font.Font(None, 100)
    font2 = pygame.font.Font(None, 20)

inside_circle = 0
total = 0

while playing:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False

        if event.type == KEYDOWN:
            if event.key == 32:
                pass

    for _ in range(10000):
        x, y = random_point()
        if dist_to_center(x, y) <= window_height / 2:
            pygame.draw.circle(screen, green, (x, y), 1)
            inside_circle += 1
        else:
            pygame.draw.circle(screen, blue, (x, y), 1)
        total += 1

    pi = 4 * inside_circle / total

    txt = font2.render(f"{pi:.6f}", True, white, black)
    txt_rect = txt.get_rect()
    txt_rect.center = (window_length // 2, window_height // 2)
    screen.blit(txt, txt_rect)

    pygame.display.update()

pygame.quit()
exit()
