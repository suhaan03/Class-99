import os 
import shutil

source = input("Enter source folder: ")
destination = input("Enter destination folder: ") 

source=source+"/"
destination=destination+'/'

listoffiles=os.listdir(source)
for file in listoffiles:
    shutil.copy((source+file),destination)