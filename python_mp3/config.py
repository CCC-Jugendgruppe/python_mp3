import os
import json
from python_mp3.log import Log


class Config:
	def __init__(self, filename):
		self.log = Log()
		self.filename = filename
		self.defaultconfig = \
			{
				"dir": [
					"/home/$USER/music",
					"/home/$USER/musik",
					"./input/"
				],
				"mp3_version": 2
			}

	def createnew(self, force=bool(1)):
		"""
			Create a new file containing the default config
			if force is true overwrites the current file if its false only appends the default config
		"""
		try:
			with open(self.filename, 'x' if force else 'a') as writer:
				writer.write(str(self.defaultconfig).replace("'", "\""))
				self.log.info("file " + self.filename + " created")
		except Exception as e:
			print("[Error]: could not create the file " + self.filename + " : " + str(e))

	def readfile(self, item=None):
		self.log.info("Filename: " + str(self.filename))
		try:
			with open(str(self.filename), 'r') as reader:
				output = reader.read()
		except FileNotFoundError:
			self.log.warning("The file " + self.filename + " does not exist but creating it")
			self.createnew(False)

		return self.__parsejson(output, item)

	def clear(self):
		if os.path.exists(str(self.filename)):
			os.remove(str(self.filename))
		else:
			self.log.error("The file " + self.filename + " does not exist")

	def update(self, content, item=None):
		"""
		This function takes the item name in the json and the new updated content.
		Please use the readfile function for the before state.
		"""
		jsonout = None
		if item is not None:
			with open(str(self.filename), 'r') as reader:
				output = reader.read()
				jsonout = self.__parsejson(output)
				jsonout[str(item)] = content
		else:
			with open(str(self.filename), 'w') as writer:
				if item is None:
					writer.write(str(jsonout).replace("'", "\""))
				else:
					writer.write(str(content).replace("'", "\""))

	def __parsejson(self, rawdata, item=None):
		# local function for formatting the json from a string
		try:
			jsonobj = json.loads(rawdata)
			if item is None:
				return jsonobj
			else:
				return jsonobj[item]
		except Exception as e:
			self.log.error("The object " + item if item is not None else "ALL" + " couldn't be found: " + str(e))
			return False


	def reset(self):
		with open(self.filename, 'w') as writer:
			writer.write(str(self.defaultconfig).replace("'", "\""))
			print("Resetting Config")
