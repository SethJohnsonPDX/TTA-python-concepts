from datetime import datetime
import time
import shutil
import os

##define source and destination directories for files we want to move
root_path = '/Users/sethjohnson/Desktop/recentlyEditedFiles'
source_path = '/Users/sethjohnson/Desktop/recentlyEditedFiles/sourceFolder'
edits_path = '/Users/sethjohnson/Desktop/recentlyEditedFiles/dailyEdits'

##use listdir to add all contents of the above source directory to a list and
source_contents = os.listdir(source_path)

##define current time and define one day (24 hours) in seconds since the epoch 
current_time = time.time()
day = 86400
marker = current_time - day

##use for loop to check that each file 
for files in source_contents:
    if files.endswith('.txt') and os.path.getmtime(os.path.join(source_path, files)) > marker:
        shutil.move(os.path.join(source_path, files), os.path.join(edits_path, files))
