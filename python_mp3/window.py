# Links
#   https://zetcode.com/pyqt6/
#
# use 'python-mp3 --gui' to execute
#
# 1. Generate Layout
# 2. Define widgets
# 3. Add widget to layout
# 4. Add widget to frame or window
# 5. Show window

import pathlib
import sys
import time

import PyQt6.QtCore as qtc
import PyQt6.QtGui as qtg
import PyQt6.QtWidgets as qtw

from python_mp3.config import Config
# python_mp3.<file> needed for proper pip implementation
from python_mp3.core import songsupdate
from python_mp3.database import Database

# TODO get system cache and config path and put files in respective folder
# Set path for temporary database to cache 
# tmp_db_path = str(pathlib.Path.home()) + '/.cache/python_mp3_tmp.sql'
tmp_db_path = 'songs.sql'
# read configurations
config_path = './config.json'
conf = Config(config_path)


def get_dirs() -> str:
	return conf.readfile(item="dir")


settings = {}


class WorkerThread(qtc.QObject):
	signalRefreshTable = qtc.pyqtSignal()

	def __init__(self) -> None:
		super().__init__()

	@qtc.pyqtSlot()
	def run(self) -> None:
		while True:
			# Long running task ...
			self.signalRefreshTable.emit()
			time.sleep(5)


class Window(qtw.QWidget):
	def __init__(self) -> None:
		super().__init__()
		self.initui()
		self.worker = WorkerThread()
		self.workerThread = qtc.QThread()
		self.workerThread.started.connect(self.worker.run)  # Init worker run() at startup (optional)
		self.worker.signalRefreshTable.connect(self.initui)  # Connect your signals/slots
		self.worker.moveToThread(self.workerThread)  # Move the Worker object to the Thread object

	# self.config = Config(config_path)
	# conf = self.config.readfile()
	# self.dirs = conf["dir"]
	# print("dirs"+self.dirs)
	# self.mp3v = self.config.readfile("mp3_version")
	# self.settings = {}

	def initui(self) -> None:
		# Global Settings
		self.setGeometry(0, 0, 650, 500)
		self.setWindowTitle('Python mp3')
		self.setFont(qtg.QFont('SansSerif', 10))

		# self.config.readfile()
		# self.loadSettings()
		# print(self.settings)

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

		"""
		self.__timer == qtc.QTimer()
		self.__timer.timeout.connect(self.show)
		self.__timer.start(1000)
		
		"""
		self.show()

	def outputFrame(self) -> qtw.QFrame:
		# General Layout Settings
		layout = self.__setupLayout('v')
		# Songs Label
		songslabel = self.__titleLabel('Songs')
		layout.addWidget(songslabel)

		# Button to Refresh Database
		refreshbtn = qtw.QPushButton('Refresh', self)
		refreshbtn.setToolTip('Refresh the Database')
		refreshbtn.clicked.connect(lambda: self.__refreshDb(tmp_db_path))
		# TODO: Read config from settings panel
		refreshbtn.resize(refreshbtn.sizeHint())
		layout.addWidget(refreshbtn)

		# self.__createSongsTable()
		songstable = self.__createSongsTable()
		layout.addWidget(songstable)

		frame = self.__setupFrame(layout)
		return frame

	def settingsFrame(self):
		layout = self.__setupLayout('v')

		settingslabel = self.__titleLabel('Settings')
		layout.addWidget(settingslabel)

		# TODO Folder selection
		# TODO Select mp3 version

		frame = self.__setupFrame(layout)
		return frame

	def bottomPanel(self) -> qtw.QHBoxLayout:
		layout = self.__setupLayout('h')

		# Button to reset settings
		resetbtn = qtw.QPushButton('Reset Config')
		resetbtn.clicked.connect(conf.reset)
		# resetbtn.clicked.connect(self.config.createnew)
		resetbtn.resize(resetbtn.sizeHint())
		resetbtn.setToolTip('Reset configuration')
		layout.addWidget(resetbtn)

		# Button to export Database
		exportbtn = qtw.QPushButton('Export')
		# TODO Tooltip for Button
		exportbtn.clicked.connect(self.exportDb)
		layout.addWidget(exportbtn)

		importBtn = qtw.QPushButton('Import Songs', self)
		importBtn.setToolTip('Import your mp3 files')
		importBtn.clicked.connect(lambda: self.importSongs())
		layout.addWidget(importBtn)

		# Button to Quit Programm
		quitbtn = qtw.QPushButton('Quit')
		quitbtn.clicked.connect(self.quit)
		quitbtn.resize(quitbtn.sizeHint())
		quitbtn.setToolTip('Exit the Program')
		layout.addWidget(quitbtn)

		return layout

	def __createSongsTable(self) -> qtw.QTableWidgetItem:
		# TODO Table with Songs
		self.__refreshDb(tmp_db_path)
		songsdb = Database(tmp_db_path)
		songsdict = songsdb.get_items()  # I am not sure what type of variable needed for Qtablewidget
		# Please look after garbage collection when using databases
		songsdb.close_connection()
		if len(songsdict) < 1:
			return None

		# print(len(songsdict[0].keys))
		testlist = [1, 2, 3, 4]
		songstable = qtw.QTableWidget(len(songsdict), len(songsdict[0].keys()), self)
		songstable.setHorizontalHeaderLabels(["id"] + songsdb.keys)

		# print(songsdict)
		# for y in songsdict:
		# print(y.values())
		z = 0
		# Create entry for every element in dict
		for i in songsdict:
			y = 0
			for values in i.values():
				newitem = qtw.QTableWidgetItem(str(values))
				songstable.setItem(z, y, newitem)
				y += 1
			z += 1
		# for i in testlist:
		#	newitem = qtw.QTableWidgetItem(str(i))
		#	songstable.setItem(y, 1, newitem)
		#	y = y + 1

		# horHeaders = []
		#	for n, key in enumerate(sorted(songsdict)):
		#		horHeaders.append(key)
		#		for m, item in enumerate(songsdict):
		#			newitem = qtw.QTableWidgetItem(item)
		#			self.setItem(m, n, newitem)
		# 	self.setHorizontalHeaderLabels(horHeaders)
		return songstable

	def __setupLayout(self, orientation: str):
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

	def __setupFrame(self, layout: str) -> qtw.QFrame:
		frame = qtw.QFrame()
		frame.setLayout(layout)
		frame.setFrameShape(qtw.QFrame.Shape.StyledPanel)
		return frame

	def __titleLabel(self, name: str) -> qtw.QLabel:
		label = qtw.QLabel('<b>' + name + '<\b>', self)
		label.setFont(qtg.QFont('Ubuntu', 15))
		return label

	def importSongs(self) -> None:
		# write opened file to dir array in json file and don't reload everything
		songs = qtw.QFileDialog.getOpenFileName(self, "Import Songs")
		print(songs)

		"""
		with open('config.json', 'r+') as f:
			data = json.load(f)
			if type(songs) == tuple:
				data["dir"].append(songs[0])

		with open('config.json', "w") as f:
			json.dump(data, f, ensure_ascii=False)
		"""
		if type(songs) == tuple:
			conf.update(item="dirs", content=songs[0])

		self.__refreshDb(tmp_db_path)

	def exportDb(self):
		# TODO use xdg file Portal
		filename = qtw.QFileDialog.getSaveFileName(self, "Export Database", ".sql")[0]

		# check if filename ends with .sql and add extension if needed
		# TODO Is this is nessary ?
		if pathlib.Path(filename).suffix != '.sql':
			filename += '.sql'
		self.__refreshDb(filename)

	# please evaluate the nessesarity

	def __refreshDb(self, path: str) -> None:
		# print('Input:',tmp_input_path, 'Output:', tmp_db_path)
		songsupdate(get_dirs(), path, 2)

	def quit(self) -> None:
		# TODO self.saveSettings()
		# TODO Quit Dialog
		qtw.QApplication.instance().quit()
		self.workerThread.start()


def createWindow() -> None:
	app = qtw.QApplication(sys.argv)
	app.setStyle('Fusion')
	# TODO: Make color pallete
	# app.setPalette(colorpalette())
	win = Window()
	sys.exit(app.exec())
