# Links
#   https://zetcode.com/pyqt6/
#
# use 'python main.py --gui' to execute

# Hidden:
# 1. Generate Layout
# 2. Define widgets
# 3. Add widget to layout
# Shown:
# 4. Add widget to frame or window



import json
import os
import pathlib
import sys

import PyQt6.QtCore as qtc
import PyQt6.QtGui as qtg
import PyQt6.QtWidgets as qtw

# python_mp3.<file> needed for proper pip implementation
from python_mp3.core import songsupdate
from python_mp3.database import Database

# Set path for temporary database to cache 
tmp_db_path = str(pathlib.Path.home()) + '/.cache/python_mp3_tmp.sql'
#
#please read in the path from the config
tmp_input_path = ['./input/'] # Temporary solution until proper implementation of config file
config_path = './python_mp3.conf' # TODO Put into config path when done with implementation


class Window(qtw.QWidget):
	def __init__(self):
		super().__init__()
		self.initui()

	settings = {}

  def initui(self):
		# Global Settings
		self.setGeometry(0, 0, 650, 500)
		self.setWindowTitle('Python mp3')
		self.setFont(qtg.QFont('SansSerif', 10))

		self.resetSettings()
		# self.loadSettings()
		print(self.settings)

		# General Layout
		mainlayout = qtw.QVBoxLayout()
		# Splitter between Output and Settings
		mainsplitter = qtw.QSplitter(qtc.Qt.Orientation.Horizontal)
    mainsplitter.addWidget(self.outputFrame())
		mainsplitter.addWidget(self.settingsFrame())
		mainlayout.addWidget(mainsplitter)
		# Bottom
		mainlayout.addLayout(self.bottomPanel())

		self.setLayout(mainlayout)
		self.show()

	def outputFrame(self):
		# General Layout Settings
		layout = self.setupLayout('v')

		# Songs Label
		songslabel = self.titleLabel('Songs')
		layout.addWidget(songslabel)

		# Button to Refresh Database
		refreshbtn = qtw.QPushButton('Refresh', self)
		refreshbtn.setToolTip('Refresh the Database')
		#refreshbtn_refreshTmpDb = self.refreshDb(tmp_db_path)
		print(tmp_db_path)
		refreshbtn.clicked.connect(self.refreshDb(tmp_db_path))
		# TODO: Read config from settings panel
		refreshbtn.resize(refreshbtn.sizeHint())
		layout.addWidget(refreshbtn)
		
		#self.createSongsTable()
		# songstable = self.createSongsTable()
		# songstable.show()
		# leftlayout.addWidget(songstable)

		frame = self.setupFrame(layout)
		return frame

	def settingsFrame(self):
		layout = self.setupLayout('v')

		settingslabel = self.titleLabel('Settings')
		layout.addWidget(settingslabel)
		
		# TODO Folder selection
		# TODO Select mp3 version

		frame = self.setupFrame(layout)
		return frame

	def bottomPanel(self):
		layout = self.setupLayout('h')

		# Button to reset settings
		resetbtn = qtw.QPushButton('Reset')
		resetbtn.clicked.connect(self.resetSettings)
		resetbtn.resize(resetbtn.sizeHint())
		resetbtn.setToolTip('Reset configuration')
		layout.addWidget(resetbtn)

		# Button to export Database
		exportbtn = qtw.QPushButton('Export')
		# TODO: export function
		exportbtn.clicked.connect(self.exportTmpDb)
		layout.addWidget(exportbtn)

		# Button to Quit Programm
		quitbtn = qtw.QPushButton('Quit')
		quitbtn.clicked.connect(self.quit)
		quitbtn.resize(quitbtn.sizeHint())
		quitbtn.setToolTip('Exit the Programm')
		layout.addWidget(quitbtn)

		return layout

	def createSongsTable(self):

		# TODO List with Songs
		self.refreshTmpDb()
		songsdb = Database(tmp_db_path)
		songsdict = songsdb.get_items() # I am not sure what type of variable needed for Qtablewidget
		print("test " + str(songsdict))

	# print(len(songsdict))

	# songstable = qtw.QTableWidget()
	# songstable.setRowCount(len(songsdict))
	# horHeaders = []
	# for n, key in enumerate(sorted(songsdict)):
	#	horHeaders.append(key)
	#	for m, item in enumerate(songsdict):
	#		newitem = qtw.QTableWidgetItem(item)
	#		self.setItem(m, n, newitem)
	# self.setHorizontalHeaderLabels(horHeaders)

	# return songstable

	def setupLayout(self, orientation):
		if orientation == 'v':
				layout = qtw.QVBoxLayout()
		elif orientation == 'h':
				layout = qtw.QHBoxLayout()
		else:
				sys.exit('setupLayout: orientation must be \'v\' or \'h\'')
		layout.setContentsMargins(0, 0, 0, 0)
		layout.setSpacing(0)
		layout.setEnabled(True)
		return layout

	def setupFrame(self, layout):
		frame = qtw.QFrame()
		frame.setLayout(layout)
		frame.setFrameShape(qtw.QFrame.Shape.StyledPanel)
		return frame

	def titleLabel(self, name):
		label = qtw.QLabel('<b>' + name + '<\b>', self)
		label.setFont(qtg.QFont('Ubuntu', 15))
		return label

	def exportDb(self):
		filename = qtw.QFileDialog.getSaveFileName(self,"Export Database","")
		print(filename)
		self.refreshDb(filename)
		
	
	def refreshDb(self,path):
		# print('Input:',tmp_input_path, 'Output:', tmp_db_path)
		# FIXME Read input paths from setings
		songsupdate(self.settings.get('paths'),path, 2)

	def quit(self):
		self.saveSettings()
		# TODO Quit Dialog
		qtw.QApplication.instance().quit()

	def resetSettings(self):
		print('Resetting Configuration')
		self.settings = {
			'paths': ['./input'],
			'mp3_version': 2
		}
		print(self.settings)

	def saveSettings(self):
		print('Saving settings... ' + str(self.settings))
		with open(config_path, 'w', encoding='utf8') as f:
			f.write(json.dumps(self.settings, indent=2, ensure_ascii=False))

	def loadSettings(self):
		print('Loading settings...')
		if os.path.isfile(config_path):
			with open(config_path, 'r', encoding='utf8') as f:
				self.settings = json.load(f)
		else:
				self.resetSettings()
		print('Loaded settings... ' + str(self.settings))
        

def createWindow():
	app = qtw.QApplication(sys.argv)
	app.setStyle('Fusion')
	# app.setPalette(colorpalette())
	win = Window()
	# win.saveSettings()
	sys.exit(app.exec())
