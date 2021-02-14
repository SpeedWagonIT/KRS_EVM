from tkinter import *
import tkinter as tk
import _func_module as fm
root = Tk()

c = Canvas(root, width=1280, height=1024, bg='white')
c.pack()

c.create_line(20, 20, 20, 180)
c.create_line(20, 180, 180, 180)
c.create_line(180, 180, 180, 20)
c.create_line(180, 20, 20, 20)

c.create_text(80, 80,
              text="1\n2\n3\n4",
              justify=CENTER, font="Verdana 15")
fm._hello()
root.mainloop()