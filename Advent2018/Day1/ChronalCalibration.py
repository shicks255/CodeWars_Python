import os
import sys
from functools import reduce

os.chdir(sys.path[0])
file = open("frequencies.txt")
frequencies = file.readlines()
frequencies = [int(x.rstrip('\n')) for x in frequencies]

answer = reduce((lambda x, y: x + y), frequencies)
print(answer)