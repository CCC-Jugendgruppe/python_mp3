# Links
#   https://zetcode.com/pyqt6/

import classes.core as c
import sys
import PyQt6.QtWidgets as qtw
import PyQt6.QtGui as qtg

class Window(qtw.QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		
		# set global style 
		self.setFont(qtg.QFont('SansSerif', 10))

		# Songs Label
		songslabel = qtw.QLabel('Songs', self)
		songslabel.setFont('Ubuntu',15)

		# button to refresh database
		refreshbtn = qtw.QPushButton('Refresh', self)
		refreshbtn.setToolTip('Refresh the Database')
		refreshbtn.clicked.connect(c.songsupdate)
		refreshbtn.resize(refreshbtn.sizeHint())
		refreshbtn.move(10, 10)

		#TODO List with Songs
		

		# Button to quit Programm 
		quitbtn = qtw.QPushButton('Quit', self)
		quitbtn.clicked.connect(qtw.QApplication.instance().quit)
		quitbtn.resize(quitbtn.sizeHint())
		quitbtn.setToolTip('Exit the Programm')
		quitbtn.move(210, 170)

		self.setGeometry(300, 300, 300, 200)
		self.setWindowTitle('Tooltips')
		self.show()

def main():
	app = qtw.QApplication(sys.argv)
	win=Window()
	sys.exit(app.exec())
		
if __name__ == '__main__':
	main()
