import pygame
import random
import math


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
        self.max_force = 0.01
    
    def update(self):
        self.position.add_vector(self.velocity) 
        self.velocity.add_vector(self.acceleration)

    #### Craig Reynolds model ####
    # steer to avoid crowding local flockmates
    def separation(self):
        pass
        #TODO

    # steer towards the average heading of local flockmates
    def align(self, boids):
        #avg = Vector()
        steering = Vector()
        perception_align = 20
        count = 0
        for b in boids:
            distance = dist(self.position.x, self.position.y, b.position.x, b.position.y)
            if b != self and distance < perception_align:
                steering.add_vector(b.velocity)
                count += 1
        if count > 0:
            steering.set_magnitude(1 / count) # Multiplica o vetor por uma constante k (nesse caso: 1/count)
            steering.sub_vector(self.velocity)
            steering.limit(self.max_force)
        return steering
    
    def flocking(self, boids):
        #m = 1 # Implementação futura, massas diferentes para os boids
        alignment = self.align(boids)
        self.acceleration = alignment
    
    # steer to move toward the average position of local flockmates
    def cohesion(self):
        pass
        #TODO

    def show(self): 
        pass
        #TODO
        #pygame.draw.circle(window, red, (p2.x, p2.y), p2.r)

def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))