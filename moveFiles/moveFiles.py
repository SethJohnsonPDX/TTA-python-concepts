import shutil

origin_random_1 = '/Users/sethjohnson/Desktop/folder-a/random_1.txt'
dest_random_1 = '/Users/sethjohnson/Desktop/folder-b/random_1.txt'
origin_random_2 = '/Users/sethjohnson/Desktop/folder-a/random_2.txt'
dest_random_2 = '/Users/sethjohnson/Desktop/folder-b/random_2.txt'
origin_random_3 = '/Users/sethjohnson/Desktop/folder-a/random_3.txt'
dest_random_3 = '/Users/sethjohnson/Desktop/folder-b/random_3.txt'
origin_random_4 = '/Users/sethjohnson/Desktop/folder-a/random_4.txt'
dest_random_4 = '/Users/sethjohnson/Desktop/folder-b/random_4.txt'

shutil.move(origin_random_1, dest_random_1)
print("Your file has been moved to ", dest_random_1)

shutil.move(origin_random_2, dest_random_2)
print("Your file has been moved to ", dest_random_2)

shutil.move(origin_random_3, dest_random_3)
print("Your file has been moved to ", dest_random_3)

shutil.move(origin_random_4, dest_random_4)
print("Your file has been moved to ", dest_random_4)
