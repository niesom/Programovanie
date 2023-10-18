import tkinter
c = tkinter.Canvas(width=500, height=500)
c.pack()
x = 250
y = 250
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
direction = 0
while current_length<TOTAL_LENGTH:
    if direction==0:
        c.create_line(x,y,x,y-LINE_LENGTH)
        y = y-LINE_LENGTH
    elif direction==1:
        c.create_line(x,y,x-LINE_LENGTH,y)
        x = x-LINE_LENGTH
    elif direction==2:
        c.create_line(x,y,x,y+LINE_LENGTH)
        y = y+LINE_LENGTH
    else:
        c.create_line(x,y,x+LINE_LENGTH,y)
        x = x+LINE_LENGTH
    direction = (direction + 1) % 4
    current_length += LINE_LENGTH
    LINE_LENGTH += INCREMENT
    if current_length + LINE_LENGTH > TOTAL_LENGTH:
        LINE_LENGTH = TOTAL_LENGTH - current_length
c.mainloop()