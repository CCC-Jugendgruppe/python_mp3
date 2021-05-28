import sqlite3
from sqlite3 import Error
import traceback

class Database:
	def __init__(self, db_file):
		print("Database file" + str(db_file))
		self.db_file = db_file  
	def create_connection(self):
		""" Create a database connection to a SQLite database."""
		print("Opening " + str(self.db_file))
		try:
			conn = sqlite3.connect(self.db_file)
			print("Done current Sqlite Version: " + str(sqlite3.version) + "\n")
		except Error as e:
			print(e)
		finally:
			return conn

	def close_connection(self, connection):
			if connection != None:
				connection.close()
				print("close DB connection")

	def init_database(self, connection):
			connection.execute('''CREATE TABLE IF NOT EXISTS music 
				(artist TEXT NULL, 
				band TEXT NULL, 
				album TEXT NULL, 
				title TEXT NULL UNIQUE, 
				track TEXT NULL UNIQUE, 
				genre TEXT NULL, 
				composer TEXT NULL, 
				copyright TEXT NULL, 
				comment TEXT NULL,
				releaseyear INT NULL,
				mp3_url TEXT NULL
				);''')
			connection.commit()
			print("Done")    

	def update_database(self, connection, data):
		sql = " INSERT INTO music (artist, band, album, title, track, genre, composer, copyright, comment, releaseyear, mp3_url) VALUES (?,?,?,?,?,?,?,?,?,?,?)"
		vallist = []
		keys = ["artist", "band", "album", "song", "track", "genre", "composer", "copyright", "comment", "year", "url"]
		i = 0

		for i in range(len(keys)):        
			try:
				#print(a[keys[i]])
				vallist.append(data[keys[i]])
			except KeyError:
				#print("novalue")
				vallist.append(None)

		#print("\n")
		#print(vallist)
		try: 
			connection.execute(sql, vallist)
			connection.commit()
		except sqlite3.IntegrityError:
			pass
