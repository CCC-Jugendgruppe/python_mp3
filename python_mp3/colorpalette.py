# https://stackoverflow.com/questions/48256772/dark-theme-for-qt-widgets

import PyQt6.QtGui as qtg


def colorpalette():
	darkpalette = qtg.QPalette()
	darkpalette.setColor(qtg.QPalette.window, qtg.QColor(53, 53, 53))
	darkpalette.setColor(qtg.QPalette.windowText, qtg.Qt.white)
	darkpalette.setColor(qtg.QPalette.base, qtg.QColor(25, 25, 25))
	darkpalette.setColor(qtg.QPalette.alternateBase, qtg.QColor(53, 53, 53))
	darkpalette.setColor(qtg.QPalette.toolTipBase, qtg.Qt.black)
	darkpalette.setColor(qtg.QPalette.toolTipText, qtg.Qt.white)
	darkpalette.setColor(qtg.QPalette.text, qtg.Qt.white)
	darkpalette.setColor(qtg.QPalette.button, qtg.QColor(53, 53, 53))
	darkpalette.setColor(qtg.QPalette.buttonText, qtg.Qt.white)
	darkpalette.setColor(qtg.QPalette.brightText, qtg.Qt.red)
	darkpalette.setColor(qtg.QPalette.link, qtg.QColor(42, 130, 218))
	darkpalette.setColor(qtg.QPalette.highlight, qtg.QColor(42, 130, 218))
	darkpalette.setColor(qtg.QPalette.highlightedText, qtg.Qt.black)
	return darkpalette
