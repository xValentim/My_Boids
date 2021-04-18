import pygame
import numpy
import math
import random
from values import *
from boid import *

pygame.init()
r = 3 # Tamanho do boid

flock = []
# Init boids
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
                # Cria boids // k está em values
                for i in range(k):
                    #b = Boid(largura / 2, altura / 2, 0, 0)
                    b = Boid(random.randint(20, largura - 20), random.randint(20, altura - 20), 0, 0)
                    b.velocity.createRandom2D()
                    #b.velocity.createRandom2D_mag1()
                    b.velocity.set_magnitude(1.5)
                    flock.append(b)
            if event.key == pygame.K_o:
                if len(flock) > 0:
                    # Aniquila boids // k está em values
                    for i in range(k):
                        flock.remove(flock[0])
    window.fill(gray)
    for b0 in flock:
        b0.flocking(flock)
        b0.update()
    for b0 in flock:
        pygame.draw.circle(window, b0.color, (b0.position.x, b0.position.y), r)
    relogio.tick(60)
    pygame.display.update()

pygame.quit()