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
        if os.path.exists(str(self.filename)):
            os.remove(str(self.filename))
        else:
            print("The file does not exist")


test = Config("/config.json")
test.readfile()
