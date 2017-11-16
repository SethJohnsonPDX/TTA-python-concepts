import shutil
import os


origin_random_1 = '/Users/sethjohnson/Desktop/folder-a/'
dest_random_1 = '/Users/sethjohnson/Desktop/folder-b/'

contents_a = os.listdir(origin_random_1)


for files in contents_a:
    if files.endswith('.txt'):
        shutil.move(os.path.join(origin_random_1, files), os.path.join(dest_random_1, files))
        
    
        


