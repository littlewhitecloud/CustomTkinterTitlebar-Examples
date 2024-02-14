from customtitlebar import CTT
from darkdetect import isDark
from tkinter.ttk import Entry
from sv_ttk import set_theme  # Optional, You can use other theme

example = CTT()
example.title("CTT example")  # Optional
example.geometry("980x560")  # Optional
entry = Entry(example.titlebar, width=35)  # You can also replace with other widget
entry.pack(pady=2, padx=2, fill="y")
if isDark():
    set_theme("dark")
else:
    set_theme("light")
example.mainloop()
