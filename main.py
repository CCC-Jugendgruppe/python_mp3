import argparse
from window import Window 
from database import Database

#test1 = Database("output/songs.sql")
#test = test1.get_items()
#print(test)
#test1.close_connection()

windowinstance = Window()
windowinstance.run()