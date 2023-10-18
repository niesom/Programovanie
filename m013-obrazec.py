import tkinter
import math
c = tkinter.Canvas(width=600, height=600)
c.pack()
x = 300
y = 300
current_length = 0
string = input("Zadaj tri cisla oddelene medzerou: ") + " "
arr = []
temp = ""
for index in range(len(string)):
    if string[index]==" ":
        arr += [int(temp)]
        temp = ""
    else:
        temp += string[index]
LINE_LENGTH = arr[0]
INCREMENT = arr[1]
TOTAL_LENGTH = arr[2]
ANGLE = 45
direction = 0
while current_length<TOTAL_LENGTH:
    move_x = math.cos(math.radians(ANGLE)) * LINE_LENGTH
    move_y = math.sin(math.radians(ANGLE)) * LINE_LENGTH
    if direction==0:
        c.create_line(x,y,x-move_x,y-move_y)
        x = x-move_x
        y = y-move_y
    elif direction==1:
        c.create_line(x,y,x-move_x,y+move_y)
        x = x-move_x
        y = y+move_y
    elif direction==2:
        c.create_line(x,y,x+move_x,y+move_y)
        x = x+move_x
        y = y+move_y
    else:
        c.create_line(x,y,x+move_x,y-move_y)
        x = x+move_x
        y = y-move_y
    direction = (direction + 1) % 4
    current_length += LINE_LENGTH
    LINE_LENGTH += INCREMENT
    if current_length + LINE_LENGTH > TOTAL_LENGTH:
        LINE_LENGTH = TOTAL_LENGTH - current_length
c.mainloop()


