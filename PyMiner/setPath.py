import os.path

#More error handling to be implimented
#Support for more OS systems also desired in future

def setPath():
    checkPath = False
    while not checkPath:
        path = raw_input('Enter Path: ')
        checkPath = os.path.exists(path)
    return path
