# data types
integer = 10
float_number = 5.0
string = "aaa"
array = [10,9,8,7,6,5,4,3,2,1]
# operations
integer = 10+5
integer = 10-5
integer = 10*5
# achtung
# integer = 10*5(10+5) => integer = 10*5 * (10+5)
integer = 10/5
integer = 10//5

# for (10),(1,10),(1,10,2) intendation
for x in range(10):
    print(x)

if 10>5:
    print("a")
elif 10==3:
    print("b")
else:
    print("c")
# custom function
def add(a,b):
    return a+b

# tkinter
import tkinter
canvas = tkinter.Canvas(width=300,height=300)
canvas.pack()
canvas.create_line(0,0,150,150)
canvas.create_oval(125,125,175,175)
a = input()
