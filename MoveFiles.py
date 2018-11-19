import os
import sys
import glob
import shutil

def main():
    argv = sys.argv
    argc = len(argv)

    if (argc != 3):
        print("error!")
        print("usage: python MoveFiles.py INPUTDIR OUTPUTDIR")
        sys.exit(1)

    if (os.path.isdir("./" + argv[1]) != True):
        print("No directory " + argv[1])
        print("usage: python MoveFiles.py INPUTDIR OUTPUTDIR")
        sys.exit(1)

    if (os.path.isdir("./" + argv[2]) != True):
        print("No directory " + argv[2])
        print("usage: python MoveFiles.py INPUTDIR OUTPUTDIR")
        sys.exit(1)

    lists = glob.glob("./" + argv[1] + "/*.jpg")

    print ("move " + argv[1] + " to " + argv[2])

    for item in lists:
        print(item)
        shutil.move(item, "./" + argv[2]) 

if __name__ == "__main__":
    main()