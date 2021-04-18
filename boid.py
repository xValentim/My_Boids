import pygame
import random
import math
from values import *

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add_vector(self, u):
        self.x += u.x
        self.y += u.y

    def sub_vector(self, u):
        self.x -= u.x
        self.y -= u.y

    def set_magnitude(self, k):
        self.x = (self.x) * k
        self.y = (self.y) * k

    def createRandom2D(self):
        self.x = random.uniform(-1, 1)
        self.y = random.uniform(-1, 1)
    
    def createRandom2D_mag1(self):
        teta = random.random() * 360
        teta = math.radians(teta)
        x = math.sin(teta)
        y = math.cos(teta)
        self.x = x
        self.y = y
    
    def set_modulo(self, k):
        self.x = self.x * (k / self.modulo())
        self.y = self.y * (k / self.modulo())


    def modulo(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
    
    def limit(self, limit):
        ro = self.modulo()
        if ro > limit:
            self.set_magnitude(limit / ro)
    

class Boid:
    def __init__(self, x0, y0, vx0, vy0, color=(240, 240, 240)):
        self.position = Vector(x0, y0)
        self.velocity = Vector(vx0, vy0)
        self.acceleration = Vector(0, 0)
        self.color = color
        self.max_force = 1
        self.max_speed = 4
    
    def edges(self):
        # Boundary condition menos eficiente
        '''if self.position.x > largura:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = largura
        if self.position.y > altura:
            self.position.y = 0
        if self.position.y < 0:
            self.positiony = altura'''
        
        # Boundary condition mais eficiente
        self.position.x = (self.position.x) % largura
        self.position.y = (self.position.y) % altura

    def update(self):
        self.position.add_vector(self.velocity) 
        self.edges()
        self.velocity.add_vector(self.acceleration)
        self.velocity.limit(self.max_speed)
        self.acceleration.set_magnitude(0)

    #### Craig Reynolds model ####
    # steer to avoid crowding local flockmates
    def separation(self, boids):
        steering = Vector()
        perception_separation = 30
        count = 0
        for b in boids:
            distance = dist(self.position.x, self.position.y, b.position.x, b.position.y)
            if b != self and distance < perception_separation:
                diff = Vector()
                diff.add_vector(self.position)
                diff.sub_vector(b.position)
                diff.set_magnitude(1 / (distance * distance))
                steering.add_vector(diff)
                count += 1
        if count > 0:
            steering.set_magnitude(1 / count) # Multiplica o vetor por uma constante k (nesse caso: 1/count)
            mod = steering.modulo() 
            steering.set_magnitude(self.max_speed / mod)
            steering.sub_vector(self.velocity)
            steering.limit(self.max_force)
        return steering

    # steer towards the average heading of local flockmates
    def align(self, boids):
        steering = Vector()
        perception_align = 50
        count = 0
        for b in boids:
            distance = dist(self.position.x, self.position.y, b.position.x, b.position.y)
            if b != self and distance < perception_align:
                steering.add_vector(b.velocity)
                count += 1
        if count > 0:
            steering.set_magnitude(1 / count) # Multiplica o vetor por uma constante k (nesse caso: 1/count)
            mod = steering.modulo()
            steering.set_magnitude(self.max_speed / mod)
            steering.sub_vector(self.velocity)
            steering.limit(self.max_force)
            #steering.set_magnitude(1 / 8)
        return steering
    
    def flocking(self, boids):
        #m = 1 # Implementação futura, massas diferentes para os boids
        
        alignment_v = self.align(boids)
        cohesion_v = self.cohesion(boids)
        separation_v = self.separation(boids)
        # Principio da superposição no somatorio dos vetores de força
        self.acceleration.add_vector(alignment_v)
        self.acceleration.add_vector(cohesion_v)
        self.acceleration.add_vector(separation_v)
    
    # steer to move toward the average position of local flockmates
    def cohesion(self, boids):
        steering = Vector()
        perception_cohesion = 50
        count = 0
        for b in boids:
            distance = dist(self.position.x, self.position.y, b.position.x, b.position.y)
            if b != self and distance < perception_cohesion:
                steering.add_vector(b.position)
                count += 1
        if count > 0:
            steering.set_magnitude(1 / count) # Multiplica o vetor por uma constante k (nesse caso: 1/count)
            steering.sub_vector(self.position)
            mod = steering.modulo() 
            steering.set_magnitude(self.max_speed / mod)
            steering.sub_vector(self.velocity)
            steering.limit(self.max_force)
            #steering.set_magnitude(1 / 100)
        return steering 

    def show(self): 
        pass
        #TODO
        #pygame.draw.circle(window, red, (p2.x, p2.y), p2.r)

def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

def dist1(x1, y1, x2, y2):
    delta_y = y1 - y2
    delta_x = x1 - x2
    d1 = math.sqrt((delta_x * delta_x) + (delta_y * delta_y))
    # Analisar o caso quando "a" não existe.
    a = delta_y / delta_x
    d_total = math.sqrt(altura * altura + (altura / a) * (altura / a))
    d2 = d_total - d1
    return min([d1, d2])