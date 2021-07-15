import os
import sys

from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
from python_mp3.database import Database
from python_mp3.log import Log
import re

class  songsupdate:
	def __init__(self,input_paths: list, db_output:chr, mp3_version:int, verbose:bool):
		self.input_paths = input_paths
		self.db_output = db_output
		self.mp3_version = mp3_version
		
		self.log = Log(verbose,'CORE')
		self.connection = None
		self.db = Database(db_output,verbose)
		self.db.init_database()
		print(str(self.db.conn) + "\n")

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
		self.__scanFolders()
		self.db.close_connection()
	
	def __scanFolders(self):
		for path in self.input_paths:
			for subdir, self.input_paths, files in os.walk(path):
				for file in files:
					if re.search("\.mp3$", file):
						tags = MP3File(os.path.join(subdir, file)).get_tags()
						if int(self.mp3_version) == 2:
							self.log.verboseinfo("Selected ID3TagV2")
							if tags["ID3TagV2"] == {}:
								self.log.verboseinfo("no Metadata")
							else:
								self.log.verboseinfo(tags["ID3TagV2"])
								self.db.update_database(tags["ID3TagV2"])
							
						else:
							self.log.verboseinfo("Selected ID3TagV1")
							if tags["ID3TagV1"] == {}:
									self.log.verboseinfo("no Metadata")
							else:
								self.log.verboseinfo(tags["ID3TagV1"])
								self.db.update_database(tags["ID3TagV1"])