from CustomTkinterTitlebar import CTT, Y, isDark # Load "CTT" class (You also can load X, TOP... from custom.py)
from tkinter.ttk import Entry # From tkinter.ttk import Entry
from sv_ttk import set_theme # Optional, You can use other theme

example = CTT(theme = "light")
example.title("CTT example") # Optional
example.geometry("980x560") # Optional
# example.iconbitmap(...) # Optional
entry = Entry(example.titlebar, width = 35) # You can also replace with other widget
entry.pack(pady = 2, padx = 2, fill = Y) # You can also change a way to pack like : grid?
if not isDark(): set_theme("dark")
else: set_theme("light")
example.mainloop()
