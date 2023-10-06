import tkinter
import random
x = random.randint(300,600)
c = tkinter.Canvas(width = x, height = x)
c.pack()
f,s,t,l = "red", "blue", "yellow", "magenta"
size = random.randint(10, 20)
for y in range(0, x//2, size):
    f, s, t, l = s, t, l, f
    c.create_rectangle(y, y, x-y, x-y, fill = f)
    c.update()
    c.after(1000)
c.mainloop()