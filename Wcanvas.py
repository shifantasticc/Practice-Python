
from tkinter import *
from tkinter import messagebox

tk = Tk()

c = Canvas(tk, height =250, width= 300)

#Drawing a line
line = c.create_line(0, 20, 70, 20, fill='black')

#Drawing an arc
arc = c.create_arc(10, 140, 140, 110, start =0, extent= 150, fill='black')

#Drawing an rectangle
rectangle = c.create_rectangle(110, 150, 150, 100, fill='black')

#Drawing a oval
oval = c.create_oval(120, 160, 280, 210, fill='black')

#Drawing a polygon
polygon = c.create_polygon(250, 30, 200, 50, 230, 90)

c.pack()
tk.mainloop()
