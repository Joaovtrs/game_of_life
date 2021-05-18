from random import randint
import pygame
from pygame.locals import *


def gcd(a, b):
    if b > a:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def pi_aprox(n, co_primo, total):
    c_p = co_primo
    t = total
    for _ in range(n):
        if gcd(randint(1, 9999), randint(1, 9999)) == 1:
            c_p += 1
        t += 1
    return (6 * t / c_p) ** (0.5), c_p, t


def draw(n, fps, t):
    txt = font.render(f"{n:.6f}", True, white, black)
    txt_rect = txt.get_rect()
    txt_rect.center = (window_length // 2, window_height // 2 + 20)
    screen.blit(txt, txt_rect)

    txt2 = font2.render(f"FPS: {fps:.2f}", True, white, black)
    txt2_rect = txt2.get_rect()
    txt2_rect.topleft = (10, 10)
    screen.blit(txt2, txt2_rect)

    t /= 1000000
    txt3 = font2.render(f"Total: {t:.1f} million pairs", True, white, black)
    txt3_rect = txt3.get_rect()
    txt3_rect.topleft = (10, 40)
    screen.blit(txt3, txt3_rect)


playing = True
clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (50, 50, 50)

# Control variables
window_height = 300
window_length = 500
gride_size = 20
gride = (int(window_length / gride_size), int(window_height / gride_size))

pygame.init()
screen = pygame.display.set_mode((window_length, window_height))
pygame.display.set_caption('Pi')

try:
    font = pygame.font.Font('RobotoMono-Bold.ttf', 100)
    font2 = pygame.font.Font('RobotoMono-Bold.ttf', 20)
except FileNotFoundError:
    font = pygame.font.Font(None, 100)
    font2 = pygame.font.Font(None, 20)

co_primo = 0
total = 0

while playing:
    clock.tick(5)

    screen.fill(black)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False

        if event.type == KEYDOWN:
            if event.key == 32:
                pass

    pi, co_primo, total = pi_aprox(40000, co_primo, total)
    draw(pi, clock.get_fps(), total)

    pygame.display.update()

pygame.quit()
exit()
