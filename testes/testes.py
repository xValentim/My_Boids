import random
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
