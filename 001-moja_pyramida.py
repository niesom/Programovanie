import tkinter
import random
width = random.randint(50, 75)
sirka = width*8
vyska = width*5
c = tkinter.Canvas(width=sirka,height=vyska,bg="blue")
tehla = random.choice([10,11,12,13,14,17,18,19,20,23,24,25,28,29,31])
pocet = 0
for z in range(8):
    x = 0+z*width//2
    y = vyska-width//2*(z+1)
    for i in range(8-z):
        pocet += 1
        color = "maroon" if pocet != tehla else "blue"
        c.create_rectangle(x,y,x+width,y+width//2,fill=color)
        x=x+width
c.pack()