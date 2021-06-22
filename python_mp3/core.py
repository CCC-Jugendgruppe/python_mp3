import os
import configparser
import sys

from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
from database import Database
import re


def songsupdate(input_paths: list, db_output, mp3_version):
    # check if input_path is array
    if type(input_paths) != list:
        if type(input_paths) == str:
            print('Converting string into list...')
            input_paths = [input_paths]
        else:
            sys.exit('songsupdate: input_path has to be an Array')
    connection = None
    db = Database(db_output)
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

    for path in input_paths:
        for subdir, input_paths, files in os.walk(path):
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
