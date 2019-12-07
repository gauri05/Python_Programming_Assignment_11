print(
    ". Design automation script which accept directory name and write names of duplicate files fromthat directory into log file named as Log.txt. Log.txt file should be created into currentdirectory. ")
import hashlib
import os
import time
import sys


# from sys import *

def hashfile(path, blocksize=1024):
    afile = open(path, 'rb')
    # print("PATH HH::::",path)
    hasher = hashlib.md5()

    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    # print("BUF   " + )
    afile.close()
    return hasher.hexdigest()


def findDup(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exits = os.path.isdir(path)
    dups = {}

    if exits:
        for dirName, subDirs, fileList in os.walk(path):
            print("Current folder is:" + dirName)
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                    print("Append")
                else:
                    dups[file_hash] = [path]
                    print("ADDDD")
        return dups
    else:
        print("Invalid Path")


def printDup(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    if len(results) > 0:
        print("Duplicates found:")
        print("The following files are duplicate")
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
    else:
        print("No duplicates files found.")


def main():
    print("Application name:" + sys.argv[0])

    if len(sys.argv) != 2:
        print("Error : Invalid number of arguments")
        exit()
    if sys.argv[1] == "-h" or sys.argv[1] == "_H":
        print("This Script is used to traverse specific diretory and display checksum of files")
        exit()
    if sys.argv[1] == "-u" or sys.argv[1] == "-U":
        print("Usage : Applicationname AbsolutePath_of_Directory Extention")
        exit()
    try:
        brr = {}
        arr = {}
        arr = findDup(sys.argv[1])
        brr = printDup(arr)
        # print(brr)

    except ValueError:
        print("Error : Invalid datatype of input")
    except Exception as E:
        print("Error : Invalid input", E)
    # file.close()


if __name__ == "__main__":
    main()
