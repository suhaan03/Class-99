import os
import shutil

source = input("Enter source folder name: ")
destination = input("Enter destination folder name: ")

source = source+'/'
destination = destination+'/'

listoffiles=os.listdir(source)
for file in listoffiles: 
    shutil.move((source+file),destination)