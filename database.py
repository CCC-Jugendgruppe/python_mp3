import sqlite3
from sqlite3 import Error

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
            if conn:
                return conn
                #conn.close()
            else:
                return False
    def close_connection(self, connection):
        if connection != None:
            connection.close()
            print("close")