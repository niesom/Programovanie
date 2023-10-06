import tkinter
import random
x = random.randint(300,600)
c = tkinter.Canvas(width = x, height = x)
c.pack()
f, s, t, l = "red", "blue", "yellow", "magenta"
size = 15
for y in range(0, x//2, size):
    f,s,t,l = s,t,l,f
    c.create_rectangle(y, y, x-y, x-y, fill = f)
