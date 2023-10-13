import math
import tkinter
import time
angle = 0
n = int(input("Zadaj počet vrcholov: "))
start = time.time()
coords = []
INCREMENT = 360/n
canvas = tkinter.Canvas(width=600, height=600)
canvas.pack()
x = 300 + math.cos(math.radians(angle))*250
y = 300 + math.sin(math.radians(angle))*250
for i in range(n):
    angle += INCREMENT
    x1 = 300 + math.cos(math.radians(angle))*250
    y1 = 300 + math.sin(math.radians(angle))*250
    coords += [(x, y)]
    canvas.create_line(x, y, x1, y1)
    x = x1
    y = y1
first, second = len(coords)-1, 1
unique_coords = []
for point in coords:
    arr = [coords[x] for x in range(len(coords)) if x!=first and x!=second and coords[x]!=point]
    first = (first + 1) % len(coords)
    second = (second + 1) % len(coords)
    for x in arr:
        unique_coords += [((point[0], point[1]),(x[0], x[1]))]
unique_coords = [tuple(sorted(x)) for x in unique_coords]
unique_coords = set(unique_coords)
for x in unique_coords:
    canvas.create_line(x[0][0], x[0][1], x[1][0], x[1][1])
    canvas.update()
    canvas.after(500)
canvas.mainloop()