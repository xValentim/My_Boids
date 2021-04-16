from testes import *

v = Vector(1, 1)
u = Vector(2, 2)
v.add_vector(u)
v_copy = (v.x, v.y)
print(v_copy)

v = Vector(1, 1)
u = Vector(2, 2)
v.sub_vector(u)
v_copy = (v.x, v.y)
print(v_copy)

v = Vector(1, 1)
u = Vector(2, 2)
v.set_magnitude(5)
v_copy = (v.x, v.y)
print(v_copy)

v = Vector()
v.createRandom2D()
v.set_magnitude(0.1)
v_copy = (v.x, v.y)
print(v_copy)