import os


def createfile(name,content):
    if content == '':
        pass
    else:
        with open(name,'a') as file:
            file.write(content)
def readfile(name):
    with open(name,'r') as file:
        read = file.read()
        return read
def delfile(name):
    os.remove(name)