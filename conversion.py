import pyembroidery
from pathlib import Path
import os

directory = r'C:\Users\K ROHIT\Downloads'
destination = 'C:/Users/K ROHIT/Downloads/converted/'


def main():
    #Checking the directory for files with given format.
    for subdir, dirs, files in os.walk(directory): 
        for filename in files:
            filepath = subdir + os.sep + filename
            if filepath.endswith(".dst") or filepath.endswith(".DST"):
                #splitting head and tail from filepath
                head, tail = os.path.split(filepath)
                fileName = tail.split(".")
                #Attaching folder name from head
                folderName = os.path.basename(os.path.normpath(head))
                #Temp directory name to check if exists
                dir_= destination + folderName
                #Convert if path exists else creates path and continues iteration.
                if os.path.exists(dir_):
                    pyembroidery.convert(filepath, dir_ + '/' + fileName[0] + '.jef')
                else:
                    os.makedirs(dir_)
                    pyembroidery.convert(filepath, dir_ + '/' + fileName[0] + '.jef')

    print("Task completed!!")                
                    

if __name__ == '__main__':
    main()
