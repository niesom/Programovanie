import math
import tkinter
import random
angle = 0
n = random.randint(3,15)
INCREMENT = 360/n
canvas = tkinter.Canvas(width=600, height=600)
canvas.pack()
x = 300 + math.cos(math.radians(angle)) * 250
y = 300 + math.sin(math.radians(angle)) * 250
for i in range(n):
    angle += INCREMENT
    x1 = 300 + math.cos(math.radians(angle)) * 250
    y1 = 300 + math.sin(math.radians(angle)) * 250
    canvas.create_line(x,y,x1,y1)
    x = x1
    y = y1
canvas.create_text(300,300,text=str(n), font="Arial 30 bold")
canvas.mainloop()
