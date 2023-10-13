import math
import tkinter
angle = -180
word = input("Zadaj slovo: ")
n = len(word)
central_angle = 2*180/n
a = math.sin(math.radians(central_angle)/2) * 250 * 2
SIZE = a/2
FONT_SIZE = int(SIZE/1.5)
INCREMENT = 360/n
canvas = tkinter.Canvas(width=800, height=800)
canvas.pack()
color = ["red","blue"]
for i in range(n):
    x = 400 - math.cos(math.radians(angle)) * 250
    y = 400 + math.sin(math.radians(angle)) * 250
    canvas.create_oval(x-SIZE, y-SIZE, x+SIZE, y+SIZE, fill = color[i%2])
    canvas.create_text(x,y, text = word[i], font=f"Arial {FONT_SIZE} bold")
    angle += INCREMENT
canvas.mainloop()
