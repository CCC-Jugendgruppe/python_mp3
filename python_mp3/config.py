
class Config:
    def __init__(self, filename):
        self.filename = filename

    def readfile(self):
        with open('dog_breeds.txt', 'r') as reader:
            print(reader.read())
        print("createnew")

    def createnew(self):
        print("createnew")

    def update(self):
        print("update")

    def clear(self):
        print("clear")
