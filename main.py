import argparse
import classes.window as w 
from classes.database import Database
from sys import exit
import PyQt6.QtWidgets
from classes.core import songsupdate
# example for getting the current saved data in the database
"""
test1 = Database("songs.sql")
test = test1.get_items()
print(test)
test1.close_connection()
"""

parser = argparse.ArgumentParser(description='Convert Songs into an Database')
parser.add_argument('-g','--gui', action='store_true', help='Open GUI')
parser.add_argument('-i','--input', dest='input_path', nargs='+', help='Path to your Music Libary')
parser.add_argument('-o','--output', dest='output_path', default='./songs.sql', help='Set output path (Default: ./songs.sql)')
parser.add_argument('--mp3-version', dest='mp3_version', choices=['1','2'], default='2', help='Set mp3 version')

args = parser.parse_args()
print(args)
#if args.help: 
#	parser.print_help
if args.gui:
	w.main()
elif args.input_path:
	songsupdate(args.input_path,args.output_path,args.mp3_version)
else:
	parser.print_help
