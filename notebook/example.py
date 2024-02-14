from tkinter.ttk import Notebook, Button
from tkinter import Frame
from tkinter.messagebox import showerror
from customtitlebar import CTT
from os import getcwd
from PIL import Image, ImageTk
from sv_ttk import set_theme
from darkdetect import isDark

value = 0


def newtab():
    global value
    if value == 11:
        showerror("Error", "Sorry, you had reached the limit")
    else:
        newframe = Frame(nb, bg="#000000")
        newframe.pack(fill="x", side="top")
        nb.add(newframe, text="Tab %d" % value)
        value += 1


ex = CTT()
ex.titlebarconfig(False, False)
ex.geometry("975x525")
ex.titlebar["height"] = 40
if isDark(): set_theme("dark")
else: set_theme("light")

newtab_load = Image.open(getcwd() +"\\newtab.png")
newtab_png = ImageTk.PhotoImage(newtab_load)
newtab = Button(ex.titlebar, image=newtab_png, command=newtab)
nb = Notebook(ex.titlebar)
nb.pack(side="left", fill="x")
nb.bind("<ButtonPress-1>", ex.dragging)
nb.bind("<B1-Motion>", ex.moving)
newtab.pack(side="left", fill="y", padx=3, pady=3)

ex.mainloop()
