from tkinter.ttk import Notebook
from tkinter.messagebox import showerror
from CustomTkinterTitlebar import CTT, getcwd, Image, ImageTk, Button, Frame, FLAT, LEFT, X, Y, TOP
from sv_ttk import set_theme
from darkdetect import isDark

value = 0
def newtab():
	global value
	if value == 11:
		showerror("Error", "Sorry, you had reached the limit")
	else:
		newframe = Frame(nb, bg= "#114514")
		newframe.pack(fill = X, side = TOP)
		nb.add(newframe, text = "Tab %d" % value)
		value += 1

ex = CTT()
ex.useicon(False)
ex.usetitle(False)
ex.geometry(975, 525)
ex.titlebar["height"] = 40
if not isDark():
	ex.bg = "#2f2f2f"
	ex.titlebar["background"] = "#2f2f2f"
	ex._titleexit["background"] = "#2f2f2f"
	ex._titlemin["background"] = "#2f2f2f"
	ex._titlemax["background"] = "#2f2f2f"
	set_theme("dark")
else:
	ex.bg = "#e7e7e7"
	ex.titlebar["background"] = "#e7e7e7"
	ex._titleexit["background"] = "#e7e7e7"
	ex._titlemin["background"] = "#e7e7e7"
	ex._titlemax["background"] = "#e7e7e7"
	ex["background"] = "#ffffff"
	set_theme("light")
	
newtab_load = Image.open("newtab.png")
newtab_png = ImageTk.PhotoImage(newtab_load)
newtab = Button(ex.titlebar, image = newtab_png, command = newtab, relief = FLAT, bg = ex.bg)
nb = Notebook(ex.titlebar)
nb.pack(side = LEFT, fill = X)
nb.bind("<ButtonPress-1>", ex.dragging)
nb.bind("<B1-Motion>", ex.moving)
newtab.pack(side = LEFT, fill = Y, padx = 3, pady = 3)

ex.mainloop()
