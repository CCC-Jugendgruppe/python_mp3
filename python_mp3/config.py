import os

class Config:
    def __init__(self, filename):
        self.filename = filename

    def readfile(self):
        print(str(self.filename))
        try:
            with open(str(self.filename), 'r') as reader:
                print(reader.read())
        except:
            print("diese Datei gibt es nicht")
            self.createnew()

    def createnew(self):
        print("createnew")

    def update(self):
        print("update")

    def clear(self):
        print("clear")


test = Config("/config.json")
test.readfile()
