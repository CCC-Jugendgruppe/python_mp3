# Links
# https://gitlab.gwdg.de/felix.schelle1/ronils/-/blob/master/gui.py
# https://tkdocs.com/tutorial/index.html
# https://www.tutorialspoint.com/python/python_gui_programming.htm

from core import songsupdate
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkf

class Window: 
	# setup
	def __init__(self):
		self.root = tk.Tk()
		self.root.title("Songs")
		mainframe = ttk.Frame(self.root, padding="3 3 12 12")
		mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
		self.root.columnconfigure(0, weight=1)
		self.root.rowconfigure(0, weight=1)

		# global font
		self.root.option_add('*font','10')
		# main window
		tk.Label(mainframe, text="Songs").grid()
		ttk.Button(mainframe,text="refresh database", command=songsupdate).grid()
		#title.option_add('*font','bold 20') TODO: Big font size for Title
		tk.Text(mainframe, width=40, height=10)
		

	def run(self):
		self.root.mainloop()

#songsupdate()
