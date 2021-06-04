import argparse
import window
import core
from database import Database

#test1 = Database("output/songs.sql")
#test = test1.get_items()
#print(test)
#test1.close_connection()

parser = argparse.ArgumentParser(description='Convert Songs into an Database')
parser.add_argument('--gui', action='store_false', help='Open the Gui')

args = parser.parse_args()
print(args)
if args.gui:
	core.songsupdate()
else:
	windowinstance = window.Window()
	windowinstance.run()
