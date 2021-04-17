import pygame
import numpy
import math
import random
from boid import *

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (35, 35, 35)
largura = 640
altura = 300
r = 5

flock = []
for i in range(0):
    b = Boid(largura / 2, altura / 2, 0, 0)
    b.velocity.createRandom2D()
    flock.append(b)

relogio = pygame.time.Clock()
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Boids")
window.fill(gray)

continua = True
while continua:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            continua = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continua = False
            if event.key == pygame.K_p:
                for i in range(10):
                    b = Boid(largura / 2, altura / 2, 0, 0)
                    b.velocity.createRandom2D()
                    flock.append(b)
            if event.key == pygame.K_o:
                if len(flock) > 0:
                    for i in range(10):
                        flock.remove(flock[0])
    window.fill(gray)

    for b0 in flock:
        b0.update()
    for b0 in flock:
        pygame.draw.circle(window, b0.color, (b0.position.x, b0.position.y), r)
    relogio.tick(60)
    pygame.display.update()

pygame.quit()