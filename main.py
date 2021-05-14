import os
import configparser
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
from database import Database

config = configparser.ConfigParser() 
config.read('config.ini')
dirs = config.items("DIRS")

if not dirs:
    print("Plase specify at least one directory in the config.ini. ")

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
            #print(os.path.join(subdir, file))
            tags = MP3File(os.path.join(subdir, file)).get_tags()
            #print(tags)
            #for i in tags:
                #print(i)
                #print(tags[i])
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

#mp3 = MP3File("audio_lib/Kygo_&_Imagine_Dragons-Born_To_Be_Yours_(Lyric Video)-mOFvJVroAJE.mp3")
# Get all tags.
#tags = mp3.get_tags()
#print(tags)

db.close_connection(connection)
