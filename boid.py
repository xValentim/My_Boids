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

class Boid:
    def __init__(self, x0, y0, vx0, vy0, color=(255, 255, 255)):
        self.position = Vector(x0, y0)
        self.velocity = Vector(vx0, vy0)
        self.acceleration = Vector(0, 0)
        self.color = color
    
    def update(self):
        self.position.add_vector(self.velocity)
        self.velocity.add_vector(self.acceleration)

    def show(self): #TODO
        pass
        #pygame.draw.circle(window, red, (p2.x, p2.y), p2.r)