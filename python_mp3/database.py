import sqlite3
import traceback
import os,sys

class Database:
	def __init__(self, db_file):
		
		"""
		if os.path.exists(db_file):
			print("test")
			print("ERROR: Database file does not exist")
			sys.exit(3)
		"""

		self.keys = ["artist", "band", "album", "song", "track", "genre", "composer", "copyright", "comment", "year", "url"]
		print("Database file " + str(db_file))
		self.db_file = db_file 		 
		""" Create a database connection to a SQLite database."""
		print("Opening " + str(self.db_file))
		try:
			self.conn = sqlite3.connect(self.db_file)
			self.c = self.conn.cursor()
			
			print("Done current Sqlite Version: " + str(sqlite3.version) + "\n")
		except sqlite3.Error as e:
			print(e)

	def close_connection(self):
		if self.conn != None:
			self.conn.close()
			print("close DB connection")

	def init_database(self):
		try:
			self.conn.execute('''CREATE TABLE IF NOT EXISTS music 
				(artist TEXT NULL,
				band TEXT NULL,
				album TEXT NULL,
				title TEXT NULL UNIQUE,
				track TEXT NULL,
				genre TEXT NULL,
				composer TEXT NULL, 
				copyright TEXT NULL, 
				comment TEXT NULL,
				releaseyear INT NULL,
				mp3_url TEXT NULL
				);''')
			self.conn.commit()
		except Exception as exc:
			print("Error: " + exc)
		print("Done")

	def update_database(self, data):
		sql = " INSERT INTO music (artist, band, album, title, track, genre, composer, copyright, comment, releaseyear, mp3_url) VALUES (?,?,?,?,?,?,?,?,?,?,?)"
		vallist = []
		for i in range(len(self.keys)):
			try:
				#print(a[keys[i]])
				vallist.append(data[self.keys[i]])
			except KeyError:
				#print("novalue")
				vallist.append(None)

		print("\n")
		print(vallist)
		try: 
			self.c.execute(sql, vallist)
			self.conn.commit()
		except sqlite3.IntegrityError as e:
			print("error when writing to the database")
			print(e)
			pass
	
	def get_items(self):
		self.c.execute('SELECT * FROM music;')		# gets all rows from table 'music'
	
		self.conn.commit()			# actually gets the items, which is needed to use retrieved items

		rows = self.c.fetchall()	# loads all selected rows from previous statement into variable 'rows'
		result = []
		for row in rows:
			index = 0
			rowdict = {}
			for cell in row:
				if cell != None:
					rowdict[str(self.keys[index])] = cell
				index = index + 1
			result.append(rowdict)
		return result #dict({"songname" : ["test", "test", "test", "test", "test","test"]})
		
#SELECT * FROM music;
