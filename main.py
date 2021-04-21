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
boid_img = pygame.image.load("boid3.png")
boid_img0 = pygame.image.load("boid3.png")
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
        #pygame.draw.circle(window, b0.color, (b0.position.x, b0.position.y), r)
        '''vector_polygon = Vector()
        vector_polygon.add_vector(b0.velocity)
        vector_polygon.set_modulo(5)
        p1 = (b0.position.x + vector_polygon.x, b0.position.y + vector_polygon.y)
        p2 = (b0.position.x + (vector_polygon.x * math.cos(math.radians(120)) - vector_polygon.y * math.sin(math.radians(120))),
              b0.position.y + (vector_polygon.x * math.sin(math.radians(120)) + vector_polygon.y * math.cos(math.radians(120))))
        p3 = (b0.position.x + (vector_polygon.x * math.cos(math.radians(300)) - vector_polygon.y * math.sin(math.radians(300))),
              b0.position.y + (vector_polygon.x * math.sin(math.radians(300)) + vector_polygon.y * math.cos(math.radians(300))))
        triangule = [p1, p2, p3]'''
        #pygame.draw.polygon(window, b0.color, triangule)
        #boid_img = pygame.transform.rotate(boid_img, random.randint(0, 359))
        boid_img = pygame.transform.scale(boid_img0, (28, 15))
        v_angle = Vector()
        v_angle.add_vector(b0.velocity)
        v_angle.set_modulo(1)
        teta = math.acos(v_angle.x)
        v = pygame.Vector2(v_angle.x, v_angle.y)
        v0 = pygame.Vector2(1, 0)
        if (v_angle.y >= 0 and v_angle.y >= 0) or (v_angle.x < 0 and v_angle.y >= 0):
            teta = math.degrees(math.acos(v_angle.x))
        else:
            teta = math.degrees(-math.acos(v_angle.x))
        boid_img = pygame.transform.rotate(boid_img, -teta)
        window.blit(boid_img, (b0.position.x, b0.position.y))
    
    relogio.tick(60)
    pygame.display.update()

pygame.quit()