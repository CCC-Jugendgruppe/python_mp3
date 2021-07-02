import os
import json
from python_mp3.log import Log
class Config:
	def __init__(self, filename):
		self.log = Log()
		self.filename = filename
		self.defaultconfig = """{
				"dir": [
					"~/music",
					"~/musik"
				],
				"mp3_version": 2
			}"""

	def createnew(self, force = bool(1)):
		"""
			Create a new file containing the default config
			if force is true overwrites the current file if its false only appends the default config
		"""
		try:
			with open(self.filename, 'x' if force else 'a') as writer:
				writer.write(self.defaultconfig)
				self.log.info("file" + self.filename + " created")
		except():
			print("[Error]: could not create the file " + self.filename)

	def readfile(self, item = None):
		self.log.info("Filename: " + str(self.filename))
		try:
			with open(str(self.filename), 'r') as reader:
				output = reader.read()
		except FileNotFoundError:
			self.log.error("The file " + self.filename + " does not exist")
			self.createnew(0)
			pass
		
		return self.__parsejson(output, item)
		

	def update(self):
		self.log.info("Updated")

	def clear(self):
		if os.path.exists(str(self.filename)):
			os.remove(str(self.filename))
		else:
			self.log.error("The file " + self.filename + " does not exist")

	def update(self, item, content):
		with open(str(self.filename), 'r') as reader:
			output = reader.read()
			json = self.__parsejson(output)
			json[str(item)] = content
			
		with open(str(self.filename), 'w') as writer:
			writer.write(str(json).replace("'","\"" ))
	
			
	def __parsejson(self, rawdata, item = None):
		try:
			jsonobj = json.loads(rawdata)
			if item == None:
				return jsonobj
			else:
				return jsonobj[item]
		except:
			self.log.error("The object " + item if item != None else "ALL" + " couldn't be found")
			return False


test = Config("config.json")
test.clear()
test.createnew()
print(test.readfile())
test.update("dir", ["test", "test3w"])