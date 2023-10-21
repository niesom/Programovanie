import tkinter
c = tkinter.Canvas(width=255, height=255)
rgb = [255,0,0]
c.pack()
for x in range(0,256,1):
    c.create_line(0,0,x,255, fill=f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}")
    c.update()
    c.after(100)
    c.create_line(0,0,255,x, fill=f"#{rgb[2]:02x}{rgb[1]:02x}{rgb[0]:02x}")
    rgb[0] -= 1
    rgb[1] += 1
c.mainloop()

import tkinter
c = tkinter.Canvas(width=255, height=255)
rgb = [255,0,0]
c.pack()
for x in range(0,255,1):
    c.create_line(0,255,255,255-x, fill=f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}")
    rgb[0] -= 1
    rgb[2] += 1
    rgb[1] += 1
for x in range(255,-1,-1):
    c.create_line(255,0,0,255-(255-x), fill=f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}")
    rgb[0] +=1 
    rgb[2] -= 1
    rgb[1] -= 1
c.mainloop()



import tkinter
c = tkinter.Canvas(width=255, height=255)
rgb = [255,255,0]
c.pack()
for x in range(0,256,1):
    c.create_line(255,255,255-x,0, fill=f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}")
    c.create_line(255,255,0,255-x, fill=f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}")
    rgb[0] -= 1
    rgb[1] -= 1
    rgb[2] += 1
c.mainloop()


import tkinter
c = tkinter.Canvas(width=255, height=255)
rgb = [0,255,0]
c.pack()
for x in range(0,256,1):
    c.create_line(255,0,0,0+x, fill=f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}")
    c.create_line(255,0,255-x,255, fill=f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}")
    rgb[0] += 1
    rgb[1] -= 1
    rgb[2] += 1
c.mainloop()