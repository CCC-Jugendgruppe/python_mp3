import argparse
import window as w 
from classes.database import Database
from sys import exit
import PyQt6.QtWidgets
from core import songsupdate
# example for getting the current saved data in the database
"""
test1 = Database("output/songs.sql")
test = test1.get_items()
print(test)
test1.close_connection()
"""

parser = argparse.ArgumentParser(description='Convert Songs into an Database')
parser.add_argument('--gui', action='store_false', help='Open the Gui')

args = parser.parse_args()
print(args)
if not args.gui:
	app=w.main()
	exit(app.exec())
else:
	songsupdate()
