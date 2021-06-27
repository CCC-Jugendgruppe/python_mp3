import os
import json


class Config:
    def __init__(self, filename):
        self.filename = filename
        self.defaultconfig = {
                "dir": [
                    "~/music",
                    "~/musik"
                ],
                "mp3_version": 2
            }

    def createnew(self, force):
        """
            Create a new file containing the default config
            if force is true overwrites the current file if its false only appends the default config
        """
        try:
            with open(str(self.filename), 'x' if force else 'a') as writer:
                writer.write(str(self.defaultconfig))
                print("file" + self.filename + " created")
        except():
            print("[Error]: could not create the file " + self.filename)

    def readfile(self, item):
        print("[Info]: Filename: " + str(self.filename))
        try:
            with open(str(self.filename), 'r') as reader:
                output = reader.read()
        except FileNotFoundError:
            print("[Error]: The file " + self.filename + " does not exist")
            self.createnew(0)
            pass
   #     try:
        jsonobj = json.loads(output)
        print(str(jsonobj))
        """
        if item == None:
            return jsonobj
        else:
            return jsonobj[item]

        except:
            print("[Error]: The object " + item if item != None else "ALL" + " couldn't be found")
"""
    def update(self):
        print("[Info]: Updated")

    def clear(self):
        if os.path.exists(str(self.filename)):
            os.remove(str(self.filename))
        else:
            print("[Error]: The file " + self.filename + " does not exist")


test = Config("config.json")
test.clear()
test.createnew(bool(0))
test.readfile("dirs")
