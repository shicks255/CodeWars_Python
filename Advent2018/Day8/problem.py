
import os
import sys

os.chdir(sys.path[0])

class Node():
    def __init__(self, header, index):
        self.childNodes = header[0]
        self.metaData = header[1]

with open("input.txt") as input:
    line = input.readlines()
    # lines = str.strip(line[0], ' ')
    license = [int(x.rstrip('\'')) for x in line[0] if x != ' ']
    print(license)


