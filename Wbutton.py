
from tkinter import *

tk = Tk()

b1 = Button(tk, text = "Submit", fg ="red")
b1.pack(side = LEFT)

b2 = Button(tk, text = "Submit", fg ="green")
b2.pack(side = TOP)

b3 = Button(tk, text = "Submit", fg ="black")
b3.pack(side = BOTTOM)

b4 = Button(tk, text = "Submit", fg ="blue")
b4.pack(side = RIGHT)

tk.mainloop()
