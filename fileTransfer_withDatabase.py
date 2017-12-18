#!/usr/bin/python3

import sqlite3
import datetime
import time
import shutil
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


class Batchfiles:



    def __init__(self, master):

        with sqlite3.connect('FBE_logs.db') as connection:
            c = connection.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS batchTime(date VARCHAR(25),
                                                            time VARCHAR(25),
                                                            count INTEGER)''')
            c.execute('SELECT * FROM batchTime ORDER BY ROWID DESC LIMIT 1')
            for row in c.fetchall():
                last_date = row[0]
                last_time = row[1]
                last_count = row[2]
            
        self.sidenav_frame = ttk.Frame(master)
        self.sidenav_frame.grid(column = 0, row = 0, padx = 15)
        
        self.logo = PhotoImage(file = 'roadvector.gif')
        ttk.Label(self.sidenav_frame, image = self.logo).grid(column = 0, columnspan = 2, row = 0)
        ttk.Label(self.sidenav_frame, text = 'Welcome to the File Batch Engine', foreground = 'dark green').grid(column = 0, row = 1, columnspan = 2, pady = 5)
        ttk.Label(self.sidenav_frame, wraplength = 300, text = ("1. Select Source Folder to find batch-able files."
                                              "\n\n2. Select Destination Folder to which you’ll copy batch files."
                                              "\n\n3. Click ‘Batch Files’ to copy all .txt files modified or created in the past 24 hours.")).grid(column = 0, row = 2, columnspan = 2)
        ttk.Label(self.sidenav_frame, text = 'Last Batch: ', foreground = 'red').grid(column = 0, rowspan = 2, row = 3)
        ttk.Label(self.sidenav_frame, text = last_date, foreground = 'red').grid(column = 1, row = 3)
        ttk.Label(self.sidenav_frame, text = last_time, foreground = 'red').grid(column = 1, row = 4)
        ttk.Button(self.sidenav_frame, text = 'Select Source Folder', command = self.select_source).grid(column = 0, row = 5, pady = 5)
        ttk.Button(self.sidenav_frame, text = 'Select Dest. Folder', command = self.select_dest).grid(column = 0, row = 6, pady = 5)
        ttk.Button(self.sidenav_frame, text = 'Batch Files', command = self.batch_files).grid(column = 0, columnspan = 2, row = 7)
        ttk.Label(self.sidenav_frame, text = 'version: 1.0\ncreator: seth johnson\ndate: 11.25.2017').grid(column = 0, row = 8, columnspan = 2, pady = 5)


    def select_source(self):
        self.varS = StringVar()
        sourceName = filedialog.askdirectory()
        self.varS.set(sourceName)
        ttk.Entry(self.sidenav_frame, textvariable = self.varS).grid(column = 1, row = 4)
        messagebox.showinfo(title = 'Source', message = 'Source has been selected.')
        

    def select_dest(self):
        self.varD = StringVar()
        desName = filedialog.askdirectory()
        self.varD.set(desName)
        ttk.Entry(self.sidenav_frame, textvariable = self.varD).grid(column = 1, row = 5)
        messagebox.showinfo(title = 'Destination', message = 'Destination has been selected.')

    def batch_files(self):
        pathS = self.varS.get()
        pathD = self.varD.get()
        source_contents = os.listdir(pathS)
        current_time = time.time()
        day = 86400
        marker = current_time - day
        file_count = len(source_contents)
        now = datetime.datetime.now()
        date_batch = now.strftime('%Y-%m-%d')
        time_batch = now.strftime('%H:%M:%S')
        for files in source_contents:
            source = os.path.join(pathS, files)
            ModifiedTime = os.path.getmtime(source)
            if files.endswith('.txt') and ModifiedTime > marker:
                shutil.move(source, pathD)
                messagebox.showinfo(title = 'File Batch Complete', message = 'Your files have been batched!')
                break
            else:
                messagebox.showinfo(title = 'File Batch Complete', message = 'No new files to batch!')
                break
        with sqlite3.connect('FBE_logs.db') as connection:
            c = connection.cursor()
            c.execute('INSERT INTO batchTime VALUES(?, ?, ?)', (date_batch, time_batch, file_count))


            
def main():            
    
    root = Tk()
    root.title('FBE 1.0')
    batchfiles = Batchfiles(root)
    root.mainloop()

                 
    
if __name__ == "__main__": main()
