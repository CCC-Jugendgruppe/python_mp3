import argparse
from window import Window 
from classes.database import Database
# example for getting the current saved data in the database
"""
test1 = Database("output/songs.sql")
test = test1.get_items()
print(test)
test1.close_connection()
"""

windowinstance = Window()
windowinstance.run()