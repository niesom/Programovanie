import tkinter
import random
d = random.randint(40, 90)
canvas = tkinter.Canvas(width=d*8,height=d*6,bg="navy")
x = 0
y = d*6
pocet = 0
tehla = random.choice([10,11,12,13,14,17,18,19,20,23,24,25,28,29,31])
for i in range(8):
    pocet = pocet + 1
    canvas.create_rectangle(x,y-d//2,x+d,y,fill="red")
    x = x + d
x = d//2
y = y-d//2
for i in range(7):
    pocet = pocet + 1
    if pocet == tehla:
        canvas.create_rectangle(x,y-d//2,x+d,y,fill="navy")
    else:
        canvas.create_rectangle(x,y-d//2,x+d,y,fill="red")
    x = x + d
x = d
y = y-d//2
for i in range(6):
    pocet = pocet + 1
    if pocet == tehla:
        canvas.create_rectangle(x,y-d//2,x+d,y,fill="navy")
    else:
        canvas.create_rectangle(x,y-d//2,x+d,y,fill="red")
    x = x + d
x = 3/2*d
y = y-d//2
for i in range(5):
    pocet = pocet + 1
    if pocet == tehla:
        canvas.create_rectangle(x,y-d//2,x+d,y,fill="navy")
    else:
        canvas.create_rectangle(x,y-d//2,x+d,y,fill="red")
    x = x + d
x = 2*d
y = y-d//2
for i in range(4):
    pocet = pocet + 1
    if pocet == tehla:
        canvas.create_rectangle(x,y-d//2,x+d,y,fill="navy")
    else:
        canvas.create_rectangle(x,y-d//2,x+d,y,fill="red")
    x = x + d
x = 5/2*d
y = y-d//2
for i in range(3):
    pocet = pocet + 1
    if pocet == tehla:
        canvas.create_rectangle(x,y-d//2,x+d,y,fill="navy")
    else:
        canvas.create_rectangle(x,y-d//2,x+d,y,fill="red")
    x = x + d
x = 3*d
y = y-d//2
for i in range(2):
    canvas.create_rectangle(x,y-d//2,x+d,y,fill="red")
    x = x + d
x = 7/2*d
y = y-d//2
for i in range(1):
    canvas.create_rectangle(x,y-d//2,x+d,y,fill="red")
    x = x + d
canvas.pack()
