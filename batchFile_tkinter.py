#!/usr/bin/python3

from datetime import datetime
import time
import shutil
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


class Batchfiles:



    def __init__(self, master):

        self.sidenav_frame = ttk.Frame(master)
        self.sidenav_frame.grid(column = 0, row = 0, padx = 15)
        
##        self.logo = PhotoImage(file = 'tour_logo.gif')
        ttk.Label(self.sidenav_frame, text = 'Welcome to the File Batch Engine').grid(column = 0, row = 0, columnspan = 2, pady = 5)
        ttk.Label(self.sidenav_frame, wraplength = 300, text = ("1. Select Source Folder to find batch-able files."
                                              "\n\n2. Select Destination Folder to which you’ll copy batch files."
                                              "\n\n3. Click ‘Batch Files’ to copy all .txt files modified or created in the past 24 hours.")).grid(column = 0, row = 1, columnspan = 2)
        ttk.Button(self.sidenav_frame, text = 'Select Source Folder', command = self.select_source).grid(column = 0, row = 2, columnspan = 2, pady = 5)
        ttk.Button(self.sidenav_frame, text = 'Select Dest. Folder', command = self.select_dest).grid(column = 0, row = 3, columnspan = 2, pady = 5)
        ttk.Button(self.sidenav_frame, text = 'Batch Files', command = self.batch_files).grid(column = 0, columnspan = 2, row = 4)

##        ttk.Label(self.sidenav_frame, image = self.logo)
        ttk.Label(self.sidenav_frame, text = 'version: 1.0\ncreator: seth johnson\ndate: 11.25.2017').grid(column = 0, row = 5, columnspan = 2, pady = 5)


    def select_source(self):
        self.varS = StringVar()
        sourceName = filedialog.askdirectory()
        self.varS.set(sourceName)
        messagebox.showinfo(title = 'Source', message = 'Source has been selected.')
        

    def select_dest(self):
        self.varD = StringVar()
        desName = filedialog.askdirectory()
        self.varD.set(desName)
        messagebox.showinfo(title = 'Destination', message = 'Destination has been selected.')

    def batch_files(self):
        source_contents = os.listdir(self.varS.get())
        current_time = time.time()
        day = 86400
        marker = current_time - day
        for files in source_contents:
            if files.endswith('.txt') and os.path.getmtime(os.path.join(self.varS.get(), files)) > marker:
                shutil.move(os.path.join(self.varS.get(), files), os.path.join(self.varD.get(), files))
                messagebox.showinfo(title = 'File Batch Complete', message = 'Your files have been batched!')
                break
            else:
                messagebox.showinfo(title = 'File Batch Complete', message = 'No new files to batch!')
                break

        

            
def main():            
    
    root = Tk()
    batchfiles = Batchfiles(root)
    root.mainloop()

                 
    
if __name__ == "__main__": main()

