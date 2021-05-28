import os
import configparser
import sys
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
from database import Database
import re

def songsupdate():
    config = configparser.ConfigParser() 
    try:
      config.read('config.ini')
    except:
      sys.exit("no config.ini found")
    try:
      dirs = config.items("DIRS")
    except:
        sys.exit("no or invalid [DIRS] section in config.ini")




    connection = None
    db = Database(config["DATABASE"]["dir"])
    connection = db.create_connection()
    db.init_database(connection)
    print(str(connection) + "\n")

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

    for key, path in dirs: 
        for subdir, dirs, files in os.walk(path):
            for file in files:
                if re.search("\.mp3$", file):
                    tags = MP3File(os.path.join(subdir, file)).get_tags()
                    if int(config["MP3"]["version"]) == 2: 
                        print("Selected ID3TagV2")
                        if tags["ID3TagV2"] == {}:
                            print("no Metadata\n")
                        else:
                            print(tags["ID3TagV2"])
                            print("\n")                
                            db.update_database(connection, tags["ID3TagV2"])
                    else: 
                        print("Selected ID3TagV1")
                        if tags["ID3TagV1"] == {}:
                            print("no Metadata\n")
                        else:
                            print(tags["ID3TagV1"])
                            print("\n")
                            db.update_database(connection, tags["ID3TagV1"])

    db.close_connection(connection)


if __name__ == "__main__":
        songsupdate()
