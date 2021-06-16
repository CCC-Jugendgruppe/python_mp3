import os
import configparser
import sys

from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
from classes.database import Database
import re

def songsupdate(songs_paths,songs_output,mp3_version):
	
	connection = None
	db = Database(songs_paths)
	db.init_database()
	print(str(db.conn) + "\n")

	"""
	Possible Tags:

		- artist;
		- album;
		- song;
		- track;
		- comment;
		- year;
		- genre;
		- band (version 2.x);
		- composer (version 2.x);
		- copyright (version 2.x);
		- url (version 2.x);
		- publisher (version 2.x).
	"""

	for key, path in songs_paths: 
		for subdir, songs_paths, files in os.walk(path):
			for file in files:
				if re.search("\.mp3$", file):
					tags = MP3File(os.path.join(subdir, file)).get_tags()
					if int(mp3_version) == 2: 
						print("Selected ID3TagV2")
						if tags["ID3TagV2"] == {}:
							print("no Metadata\n")
						else:
							print(tags["ID3TagV2"])
							print("\n")                
							db.update_database(tags["ID3TagV2"])
					else: 
						print("Selected ID3TagV1")
						if tags["ID3TagV1"] == {}:
							print("no Metadata\n")
						else:
							print(tags["ID3TagV1"])
							print("\n")
							db.update_database(tags["ID3TagV1"])

	db.close_connection()

if __name__ == "__main__":
	print("Use main.py to use program")
