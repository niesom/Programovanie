import tkinter
import math
import random
c = tkinter.Canvas(width=500,height=500)
c.pack()
for i in range(50):
    v = 30
    x = random.randint(0 + v, 500 - v)
    y = random.randint(0 + v, 500 - v)
    u = random.randint(0, 360)
    x1 = x + math.cos(math.radians(u)) * v
    y1 = y + math.sin(math.radians(u)) * v
    u = u + 120
    x2 = x + math.cos(math.radians(u)) * v
    y2 = y + math.sin(math.radians(u)) * v
    u = u + 120
    x3 = x + math.cos(math.radians(u)) * v
    y3 = y + math.sin(math.radians(u)) * v
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    c.create_polygon(x1, y1, x2, y2, x3, y3, fill= f"#{r:02x}{g:02x}{b:02x}")
c.mainloop()