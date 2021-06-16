# Links
#   https://zetcode.com/pyqt6/
#
# use 'python main.py --gui' to execute

from classes.core import songsupdate
import classes.database as db
from classes.colorpalette import colorpalette
import sys
import PyQt6.QtWidgets as qtw
import PyQt6.QtGui as qtg

tmp_db_path='~/.cache/python_mp3_tmp.db'

class Window(qtw.QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		
		# set global style 
		self.setFont(qtg.QFont('SansSerif', 10))

		# Songs Label
		songslabel = qtw.QLabel('<b>Songs<\b>', self)
		songslabel.setFont(qtg.QFont('Ubuntu', 15))
		songslabel.move(10,10)

		# button to refresh database
		refreshbtn = qtw.QPushButton('Refresh', self)
		refreshbtn.setToolTip('Refresh the Database')
		refreshbtn.clicked.connect(songsupdate('./input',tmp_db_path,2)) #TODO: Read config from settings panel
		refreshbtn.resize(refreshbtn.sizeHint())
		refreshbtn.move(10, 40)

		self.createSongstable()

		# Button to quit Programm 
		quitbtn = qtw.QPushButton('Quit', self)
		quitbtn.clicked.connect(qtw.QApplication.instance().quit)
		quitbtn.resize(quitbtn.sizeHint())
		quitbtn.setToolTip('Exit the Programm')
		quitbtn.move(215, 420)

		self.setGeometry(300, 300, 300, 450)
		self.setWindowTitle('Tooltips')
		self.show()

	def createSongstable(self):
		#TODO List with Songs
		songsupdate('~/Music',tmp_db_path,2)
		songsdb = db.Database(tmp_db_path)
		songsdb.close_connection
		songsdict = songsdb.get_items()
		#print(songsdict)
		#print(len(songsdict))

		# List or table for songs?

		#songstable = qtw.QTableWidget()
		#songstable.setRowCount(len(songsdict))
		#horHeaders = []
		#for n, key in enumerate(sorted(songsdict)):
		#	horHeaders.append(key)
		#	for m, item in enumerate(songsdict):
		#		newitem = qtw.QTableWidgetItem(item)
		#		self.setItem(m, n, newitem)
		#self.setHorizontalHeaderLabels(horHeaders)
		#songstable.show()

		#songslist = qtw.QListWidget()
		#songslist.resize(270,290)
		#songslist.move(10,5)
		#songslist.addItem('Testtest')
		#songslist.setWindowTitle('Songs')
		#songslist.show()
		#songslist.update
	
	def updatesongslist(self):
		print('test')

def main():
	
	app = qtw.QApplication(sys.argv)
	app.setStyle('Fusion')
	#app.setPalette(colorpalette)
	win=Window()
	sys.exit(app.exec())
		
if __name__ == '__main__':
	main()
