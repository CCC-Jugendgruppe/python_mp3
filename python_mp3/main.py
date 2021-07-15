from argparse import ArgumentParser
from sys import exit
from python_mp3.window import createWindow
from python_mp3.core import songsupdate
from python_mp3.log import Log

# example for getting the current saved data in the database
"""
test1 = Database("songs.sql")
test = test1.get_items()
print(test)
test1.close_connection()
"""


def main():
  parser = ArgumentParser(description='Convert Songs into an Database')
  parser.add_argument('-g', '--gui', action='store_true', help='Open GUI')
  parser.add_argument('-i', '--input', dest='input_path', nargs='+', help='Path to your Music Libary')
  parser.add_argument('-o', '--output', dest='output_path', default='./songs.sql',help='Set output path (Default: ./songs.sql)')
  parser.add_argument('-v','--verbose', action='store_true', dest='verbose', help='Enable verbose output')
  parser.add_argument('--mp3-version', dest='mp3_version', choices=['1', '2'], default='2', help='Set mp3 version')

  args = parser.parse_args()
  #if args.verbose:
  #  Log.enableverbose(Log)
  
  # Call right function
  if args.gui:
    createWindow(args.verbose)
  elif args.input_path:
    songsupdate(args.input_path, args.output_path, args.mp3_version, args.verbose)
  else:
    parser.print_help()


if __name__ == "__main__":
    exit(main())
