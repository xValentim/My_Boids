import random
from values import *
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

def dist_edge(x1, y1, x2, y2, largura, altura):
    delta_y = y1 - y2
    delta_x = x1 - x2
    d1 = math.sqrt((delta_x * delta_x) + (delta_y * delta_y))
    a = delta_y / delta_x
    d_total = math.sqrt(altura * altura + (altura / a) * (altura / a))
    d2 = d_total - d1
    return min([d1, d2])
    #total = 
