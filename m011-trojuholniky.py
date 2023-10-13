import tkinter
import math
import random

c=tkinter.Canvas(width=500,height=500)
c.pack()
for i in range(50):
    v=30
    x = random.randrange(0 + v,500 - v)
    y = random.randrange(0 + v,500 - v)
    u = random.randint(0, 360)
    arr = []
    for number in range(3):
        x1 = x + math.cos(math.radians(u)) * v
        y1 = y + math.sin(math.radians(u)) * v
        u+=120
        arr += [x1,y1]
    c.create_polygon(*arr, fill='#'+"".join([f"{random.randint(0,255):02x}" for _ in range(3)]))
c.mainloop()