
import os
import sys

os.chdir(sys.path[0])

with open('input.txt') as input:
    print(input.read())