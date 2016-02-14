import os
from path import path

def cleanup_pyc(DIRECTORY):
    d = path(DIRECTORY)
    files = d.walkfiles("*.pyc")
    for file in files:
        file.remove()
        print "Removed {} file".format(file)

if __name__ == '__main__':
    cleanup_pyc(os.getcwd())
