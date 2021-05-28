# Links
# https://gitlab.gwdg.de/felix.schelle1/ronils/-/blob/master/gui.py
# https://tkdocs.com/tutorial/index.html
# https://www.tutorialspoint.com/python/python_gui_programming.htm

from main import songsupdate
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkf

# setup
root = tk.Tk()
root.title("Songs")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# global font
root.option_add('*font','10')

# main window
title=ttk.Label(mainframe, text="Songs").grid()
#title.option_add('*font','bold 20') TODO: Big font size for Title
searchbar = tk.Text(mainframe, width=40, height=10)


root.mainloop()

#songsupdate()
